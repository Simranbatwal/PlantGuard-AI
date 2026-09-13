"""API integration tests use isolated temporary storage and a controllable clock."""

import io
import csv
import hashlib
from datetime import datetime, timezone, timedelta
from PIL import Image
import pytest
from fastapi.testclient import TestClient
from backend.app import create_app, MAX_UPLOAD


@pytest.fixture
def setup(tmp_path):
    now = [datetime(2026, 9, 13, 10, 0, tzinfo=timezone.utc)]
    with TestClient(create_app(tmp_path, clock=lambda: now[0])) as client:
        yield client, now, tmp_path


def packet(now, **changes):
    p = dict(
        node_id="PG-A",
        zone_id="A",
        boot_id="test-1",
        sequence=1,
        captured_at=now[0].isoformat(),
        source_type="simulated",
        measurements={"relative_humidity_pct": 65},
        firmware_version="test-1",
    )
    p.update(changes)
    return p


def image_bytes(size=(128, 96), fmt="JPEG"):
    buf = io.BytesIO()
    Image.new("RGB", size, (50, 130, 70)).save(buf, fmt)
    return buf.getvalue()


def test_initial_state_is_empty(setup):
    c, _, _ = setup
    assert c.get("/api/health").json()["model_status"] == "not_configured"
    o = c.get("/api/overview").json()
    assert o["reading_count"] == 0 and not o["simulator"]["running"]
    assert all(z["status"] == "no_data" and z["latest"] is None for z in o["zones"])
    assert c.get("/api/scans").json() == {"total": 0, "items": []}


def test_duplicate_collision_and_source_isolation(setup):
    c, now, _ = setup
    p = packet(now)
    first = c.post("/api/telemetry", json=p).json()
    assert not first["duplicate"]
    assert c.post("/api/telemetry", json=p).json() == {
        "id": first["id"],
        "duplicate": True,
    }
    p["measurements"]["relative_humidity_pct"] = 66
    assert c.post("/api/telemetry", json=p).status_code == 409
    p["source_type"] = "physical"
    assert c.post("/api/telemetry", json=p).status_code == 200
    assert c.get("/api/overview?source=simulated").json()["reading_count"] == 1
    assert c.get("/api/overview?source=physical").json()["reading_count"] == 1
    assert c.get("/api/overview?source=replay").json()["reading_count"] == 0


def test_late_packet_does_not_replace_current_and_eventually_offline(setup):
    c, now, _ = setup
    c.post("/api/telemetry", json=packet(now))
    old = packet(
        now, sequence=2, captured_at=(now[0] - timedelta(minutes=10)).isoformat()
    )
    assert c.post("/api/telemetry", json=old).status_code == 200
    zone = c.get("/api/overview").json()["zones"][0]
    assert zone["latest"]["sequence"] == 1 and zone["status"] == "current"
    now[0] += timedelta(seconds=181)
    assert c.get("/api/overview").json()["zones"][0]["status"] == "offline"
    old["sequence"] = 3
    c.post("/api/telemetry", json=old)
    assert c.get("/api/overview").json()["zones"][0]["status"] == "stale"


def test_missing_stays_null_and_zero_is_valid(setup):
    c, now, _ = setup
    c.post("/api/telemetry", json=packet(now, measurements={}))
    z = c.get("/api/overview").json()["zones"][0]
    assert (
        z["status"] == "missing"
        and z["latest"]["measurements"]["relative_humidity_pct"] is None
    )
    c.post(
        "/api/telemetry",
        json=packet(now, sequence=2, measurements={"relative_humidity_pct": 0}),
    )
    assert c.get("/api/overview").json()["zones"][0]["status"] == "current"


@pytest.mark.parametrize(
    "change",
    [
        {"measurements": {"relative_humidity_pct": 150}},
        {"zone_id": "B"},
        {"captured_at": "2099-01-01T00:00:00Z"},
        {"sequence": 1.5},
    ],
)
def test_invalid_messages_are_not_saved(setup, change):
    c, now, _ = setup
    assert c.post("/api/telemetry", json=packet(now, **change)).status_code == 422
    assert c.get("/api/overview").json()["reading_count"] == 0


def test_simulator_scenarios_and_source_scope(setup):
    c, now, _ = setup

    def act(action, zone="A"):
        return c.post("/api/simulator", json={"action": action, "zone": zone})

    assert act("duplicate").status_code == 409
    assert act("start").status_code == 200
    assert c.get("/api/overview").json()["reading_count"] == 2
    assert act("stop").status_code == 200
    assert act("duplicate").json()["duplicate"]
    assert act("invalid").json()["rejected"]
    assert c.get("/api/overview").json()["reading_count"] == 2
    act("missing")
    assert c.get("/api/overview").json()["zones"][0]["status"] == "missing"
    act("disconnect", "B")
    assert not c.get("/api/overview").json()["simulator"]["enabled"]["B"]
    act("reconnect", "B")
    assert c.get("/api/overview").json()["simulator"]["enabled"]["B"]
    assert c.get("/api/overview?source=physical").json()["reading_count"] == 0


def test_photo_roundtrip_context_and_persistence(setup):
    c, now, path = setup
    c.post("/api/telemetry", json=packet(now))
    b = image_bytes()
    response = c.post(
        "/api/scans",
        data={"zone": "A", "source": "simulated"},
        files={"file": ("leaf.jpg", b, "image/jpeg")},
    )
    assert response.status_code == 201, response.text
    sid = response.json()["id"]
    assert response.json()["model_status"] == "not_configured"
    photo = c.get("/api/scans").json()["items"][0]
    assert photo["sha256"] == hashlib.sha256(b).hexdigest() and photo["width"] == 128
    assert photo["context"]["reading"]["source_type"] == "simulated"
    assert "capture time is unknown" in photo["context"]["association"]
    assert c.get(photo["preview_url"]).headers["content-type"] == "image/jpeg"
    assert (path / "uploads" / (sid + ".original")).read_bytes() == b
    with TestClient(create_app(path, clock=lambda: now[0])) as restarted:
        assert restarted.get("/api/scans").json()["total"] == 1
        assert restarted.get("/api/overview").json()["reading_count"] == 1
        assert not restarted.get("/api/overview").json()["simulator"]["running"]


@pytest.mark.parametrize(
    "b,zone,code",
    [
        (b"not a picture", "A", 422),
        (image_bytes((32, 32)), "A", 422),
        (image_bytes(), "C", 422),
        (b"x" * (MAX_UPLOAD + 1), "A", 413),
    ],
    ids=["corrupt", "too_small", "invalid_zone", "too_large"],
)
def test_bad_uploads_leave_no_records_or_files(setup, b, zone, code):
    c, _, path = setup
    assert (
        c.post(
            "/api/scans",
            data={"zone": zone},
            files={"file": ("fake.png", b, "image/png")},
        ).status_code
        == code
    )
    assert c.get("/api/scans").json()["total"] == 0
    assert list((path / "uploads").iterdir()) == []


def test_csv_is_source_filtered_and_formula_safe(setup):
    c, now, _ = setup
    c.post("/api/telemetry", json=packet(now, boot_id="=danger"))
    c.post("/api/telemetry", json=packet(now, source_type="physical"))
    response = c.get("/api/export/telemetry.csv?source=simulated")
    rows = list(csv.DictReader(io.StringIO(response.text)))
    assert len(rows) == 1 and rows[0]["source"] == "simulated"
    assert rows[0]["boot_id"] == "'=danger"
    assert rows[0]["temperature_c"] == ""


def test_foreign_origin_and_untrusted_host_rejected(setup):
    c, now, _ = setup
    assert (
        c.post(
            "/api/telemetry",
            json=packet(now),
            headers={"Origin": "https://foreign.example"},
        ).status_code
        == 403
    )
    assert c.get("/api/health", headers={"Host": "foreign.example"}).status_code == 400
    assert c.get("/api/scans/not-an-id/image").status_code == 404


def test_concurrent_duplicate_requests_are_idempotent(setup):
    from concurrent.futures import ThreadPoolExecutor

    c, now, _ = setup
    payload = packet(now)
    with ThreadPoolExecutor(max_workers=6) as pool:
        responses = list(
            pool.map(lambda _: c.post("/api/telemetry", json=payload), range(12))
        )
    assert all(r.status_code == 200 for r in responses)
    assert sum(not r.json()["duplicate"] for r in responses) == 1
    assert c.get("/api/overview").json()["reading_count"] == 1
