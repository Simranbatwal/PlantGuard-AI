"""Local PlantGuard application. Disease inference is intentionally unconfigured."""

import asyncio
import contextlib
import csv
import hashlib
import io
import json
import os
import random
import sqlite3
import uuid
import warnings
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Literal
from urllib.parse import urlparse
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Query, Request
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
from PIL import Image, ImageOps, UnidentifiedImageError
from pydantic import BaseModel
from contracts.telemetry import Telemetry

ROOT = Path(__file__).resolve().parents[1]
Source = Literal["simulated", "physical", "replay"]
MAX_UPLOAD = 8 * 1024 * 1024


def utcnow():
    return datetime.now(timezone.utc)


def stamp(dt):
    return dt.astimezone(timezone.utc).isoformat()


def create_app(data_dir=None, clock=utcnow):
    directory = Path(
        data_dir or os.environ.get("PLANTGUARD_DATA_DIR", ROOT / "runtime")
    )
    directory.mkdir(parents=True, exist_ok=True)
    uploads = directory / "uploads"
    uploads.mkdir(exist_ok=True)
    db = directory / "plantguard.sqlite3"

    @contextlib.contextmanager
    def connection():
        c = sqlite3.connect(db, timeout=15)
        c.row_factory = sqlite3.Row
        try:
            with c:
                yield c
        finally:
            c.close()

    with connection() as c:
        c.execute("PRAGMA journal_mode=WAL")
        c.executescript("""CREATE TABLE IF NOT EXISTS telemetry(id INTEGER PRIMARY KEY, node TEXT NOT NULL,zone TEXT NOT NULL,source TEXT NOT NULL,boot TEXT NOT NULL,seq INTEGER NOT NULL,captured TEXT NOT NULL,received TEXT NOT NULL,payload TEXT NOT NULL,UNIQUE(source,node,boot,seq));
        CREATE INDEX IF NOT EXISTS ix_telemetry_lookup ON telemetry(source,zone,captured);
        CREATE TABLE IF NOT EXISTS scans(id TEXT PRIMARY KEY,zone TEXT NOT NULL,source TEXT NOT NULL,filename TEXT NOT NULL,uploaded TEXT NOT NULL,sha256 TEXT NOT NULL,width INTEGER,height INTEGER,format TEXT NOT NULL,context TEXT NOT NULL);
        PRAGMA user_version=1;""")
    sim = {
        "running": False,
        "enabled": {"A": True, "B": True},
        "boot": str(uuid.uuid4()),
        "sequence": 0,
        "error": None,
    }
    rng = random.Random()

    def ingest(value):
        if value.captured_at > clock() + timedelta(seconds=60):
            raise HTTPException(
                422, "Capture time is too far in the future. Check the node clock."
            )
        value = value.model_copy(
            update={"captured_at": value.captured_at.astimezone(timezone.utc)}
        )
        payload = value.model_dump_json()
        with connection() as c:
            previous = c.execute(
                "SELECT id,payload FROM telemetry WHERE source=? AND node=? AND boot=? AND seq=?",
                (value.source_type, value.node_id, value.boot_id, value.sequence),
            ).fetchone()
            if previous:
                if previous["payload"] != payload:
                    raise HTTPException(
                        409, "This message identity already contains different data."
                    )
                return {"id": previous["id"], "duplicate": True}
            cur = c.execute(
                "INSERT INTO telemetry(node,zone,source,boot,seq,captured,received,payload) VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(source,node,boot,seq) DO NOTHING",
                (
                    value.node_id,
                    value.zone_id,
                    value.source_type,
                    value.boot_id,
                    value.sequence,
                    stamp(value.captured_at),
                    stamp(clock()),
                    payload,
                ),
            )
            if cur.rowcount == 0:
                previous = c.execute(
                    "SELECT id,payload FROM telemetry WHERE source=? AND node=? AND boot=? AND seq=?",
                    (value.source_type, value.node_id, value.boot_id, value.sequence),
                ).fetchone()
                if previous["payload"] != payload:
                    raise HTTPException(
                        409, "This message identity already contains different data."
                    )
                return {"id": previous["id"], "duplicate": True}
            return {"id": cur.lastrowid, "duplicate": False}

    def reading(row):
        if row is None:
            return None
        return dict(
            id=row["id"], received_at=row["received"], **json.loads(row["payload"])
        )

    def latest(zone, source):
        with connection() as c:
            return reading(
                c.execute(
                    "SELECT * FROM telemetry WHERE zone=? AND source=? ORDER BY captured DESC,id DESC LIMIT 1",
                    (zone, source),
                ).fetchone()
            )

    def simulate(zone, scenario="normal"):
        sim["sequence"] += 1
        humidity = round(rng.uniform(59, 72) if zone == "A" else rng.uniform(72, 85), 1)
        m = {
            "air_temperature_c": round(rng.uniform(23, 29), 1),
            "relative_humidity_pct": humidity,
            "soil_moisture_raw_adc": rng.randint(1400, 2300),
            "soil_moisture_relative_pct": round(rng.uniform(38, 63), 1),
            "leaf_wetness_raw": round(rng.uniform(0, 80), 1),
            "leaf_wetness_state": "wet" if zone == "B" else "dry",
            "light_lux": round(rng.uniform(2200, 4900)),
        }
        if scenario == "missing":
            m = {}
        value = Telemetry(
            node_id="PG-" + zone,
            zone_id=zone,
            boot_id=sim["boot"],
            sequence=sim["sequence"],
            captured_at=clock() - timedelta(seconds=600 if scenario == "stale" else 0),
            source_type="simulated",
            measurements=m,
            calibration_id="SIMULATION-ONLY",
            firmware_version="sim-0.1",
        )
        return ingest(value)

    async def ticker():
        while True:
            await asyncio.sleep(10)
            if sim["running"]:
                try:
                    for zone, enabled in sim["enabled"].items():
                        if enabled:
                            simulate(zone)
                    sim["error"] = None
                except Exception:
                    sim["error"] = (
                        "Simulator could not save readings. Check available disk space and restart."
                    )
                    sim["running"] = False

    @asynccontextmanager
    async def lifespan(app):
        task = asyncio.create_task(ticker())
        yield
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await task

    app = FastAPI(title="PlantGuard Local", version="0.3.0", lifespan=lifespan)
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "testserver"]
    )

    @app.middleware("http")
    async def local_only(request: Request, call_next):
        origin = request.headers.get("origin")
        if (
            request.method not in ("GET", "HEAD", "OPTIONS")
            and origin
            and urlparse(origin).netloc != request.headers.get("host")
        ):
            return JSONResponse(
                {"detail": "Use PlantGuard from its local application address."}, 403
            )
        if request.method == "POST":
            try:
                if (
                    int(request.headers.get("content-length", "0"))
                    > MAX_UPLOAD + 1024 * 1024
                ):
                    return JSONResponse({"detail": "Upload limit is 8 MiB."}, 413)
            except ValueError:
                return JSONResponse({"detail": "Invalid content length."}, 400)
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    @app.get("/api/health")
    def health():
        return {
            "application": "PlantGuard",
            "version": "0.3.0",
            "status": "ok",
            "model_status": "not_configured",
        }

    @app.post("/api/telemetry")
    def telemetry(value: Telemetry):
        return ingest(value)

    @app.get("/api/overview")
    def overview(source: Source = "simulated"):
        zones = []
        with connection() as c:
            for zone in ["A", "B"]:
                r = latest(zone, source)
                last_contact = c.execute(
                    "SELECT MAX(received) FROM telemetry WHERE zone=? AND source=?",
                    (zone, source),
                ).fetchone()[0]
                age = (
                    max(
                        0,
                        (
                            clock() - datetime.fromisoformat(r["captured_at"])
                        ).total_seconds(),
                    )
                    if r
                    else None
                )
                offline = (
                    (clock() - datetime.fromisoformat(last_contact)).total_seconds()
                    > 180
                    if last_contact
                    else True
                )
                missing = not r or all(
                    r["measurements"].get(k) is None
                    for k in [
                        "air_temperature_c",
                        "relative_humidity_pct",
                        "soil_moisture_raw_adc",
                        "leaf_wetness_raw",
                    ]
                )
                status = (
                    "no_data"
                    if not r
                    else "offline"
                    if offline
                    else "stale"
                    if age > 180
                    else "missing"
                    if missing
                    else "current"
                )
                zones.append(
                    {
                        "zone_id": zone,
                        "status": status,
                        "age_seconds": age,
                        "last_contact": last_contact,
                        "latest": r,
                    }
                )
            count = c.execute(
                "SELECT COUNT(*) FROM telemetry WHERE source=?", (source,)
            ).fetchone()[0]
            scans = c.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
        return {
            "server_time": stamp(clock()),
            "source": source,
            "zones": zones,
            "reading_count": count,
            "scan_count": scans,
            "model_status": "not_configured",
            "simulator": {
                k: v for k, v in sim.items() if k not in ["boot", "sequence"]
            },
        }

    @app.get("/api/history")
    def history(
        zone: Literal["A", "B"] = "A",
        source: Source = "simulated",
        limit: int = Query(60, ge=1, le=500),
    ):
        with connection() as c:
            rows = c.execute(
                "SELECT * FROM telemetry WHERE zone=? AND source=? ORDER BY captured DESC,id DESC LIMIT ?",
                (zone, source, limit),
            ).fetchall()
        return [reading(r) for r in reversed(rows)]

    class SimulationCommand(BaseModel):
        action: Literal[
            "start",
            "stop",
            "sample",
            "missing",
            "stale",
            "duplicate",
            "invalid",
            "disconnect",
            "reconnect",
        ]
        zone: Literal["A", "B"] = "A"

    @app.post("/api/simulator")
    def simulator(command: SimulationCommand):
        action = command.action
        zone = command.zone
        if action == "start":
            sim["running"] = True
            for z, enabled in sim["enabled"].items():
                if enabled:
                    simulate(z)
            return {
                "message": "Simulator started. Generated readings are saved every 10 seconds."
            }
        if action == "stop":
            sim["running"] = False
            return {"message": "Simulator stopped. Saved history is retained."}
        if action in ["disconnect", "reconnect"]:
            sim["enabled"][zone] = action == "reconnect"
            return {
                "message": f"Zone {zone} simulation "
                + (
                    "enabled."
                    if sim["enabled"][zone]
                    else "paused. Existing readings will age normally."
                )
            }
        if action == "invalid":
            # Exercise the same contract used for real messages; never save invalid data.
            from pydantic import ValidationError

            try:
                Telemetry(
                    node_id="PG-" + zone,
                    zone_id=zone,
                    boot_id="invalid-test",
                    sequence=0,
                    captured_at=clock(),
                    source_type="simulated",
                    measurements={"relative_humidity_pct": 150},
                    firmware_version="sim-0.1",
                )
            except ValidationError:
                return {
                    "message": "PASS: 150% humidity was rejected. No invalid reading was saved.",
                    "rejected": True,
                }
            raise HTTPException(500, "Validation check failed")
        if action == "duplicate":
            r = latest(zone, "simulated")
            if not r:
                raise HTTPException(409, "Send one sample before testing a duplicate.")
            r.pop("id")
            r.pop("received_at")
            result = ingest(Telemetry.model_validate(r))
            return {
                "message": "Duplicate ignored; no second record was created.",
                **result,
            }
        result = simulate(zone, "normal" if action == "sample" else action)
        return {
            "message": f"{action.title()} sample saved for zone {zone}. Older timestamps never replace newer readings.",
            **result,
        }

    @app.post("/api/scans", status_code=201)
    async def upload(
        file: UploadFile = File(...),
        zone: Literal["A", "B"] = Form(...),
        source: Source = Form("simulated"),
    ):
        b = await file.read(MAX_UPLOAD + 1)
        await file.close()
        if len(b) > MAX_UPLOAD:
            raise HTTPException(413, "Image must be 8 MiB or smaller.")
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error", Image.DecompressionBombWarning)
                with Image.open(io.BytesIO(b)) as im:
                    fmt = im.format
                    if fmt not in ("JPEG", "PNG", "WEBP"):
                        raise ValueError("Use a JPEG, PNG or WebP photo.")
                    if im.width * im.height > 20_000_000:
                        raise ValueError(
                            "Image must contain at most 20 million pixels."
                        )
                    if min(im.size) < 64:
                        raise ValueError(
                            "Image must be at least 64 pixels on each side."
                        )
                    if getattr(im, "n_frames", 1) > 1:
                        raise ValueError("Use a still photo, not an animation.")
                    im.verify()
                with Image.open(io.BytesIO(b)) as im:
                    preview = ImageOps.exif_transpose(im).convert("RGB")
                    preview.load()
        except (
            ValueError,
            UnidentifiedImageError,
            OSError,
            Image.DecompressionBombError,
            Image.DecompressionBombWarning,
        ) as e:
            raise HTTPException(
                422,
                str(e)
                if isinstance(e, ValueError)
                else "This file is not a readable image.",
            )
        sid = uuid.uuid4().hex
        original = uploads / (sid + ".original")
        thumbnail = uploads / (sid + ".jpg")
        width, height = preview.size
        preview.thumbnail((1600, 1600))
        ctx = {
            "association": "Upload-time monitoring context only; photo capture time is unknown.",
            "reading": latest(zone, source),
        }
        row = (
            sid,
            zone,
            source,
            (file.filename or "photo").replace("\\", "/").split("/")[-1][:160],
            stamp(clock()),
            hashlib.sha256(b).hexdigest(),
            width,
            height,
            fmt,
            json.dumps(ctx),
        )
        try:
            original.write_bytes(b)
            preview.save(thumbnail, "JPEG", quality=90)
            with connection() as c:
                c.execute("INSERT INTO scans VALUES(?,?,?,?,?,?,?,?,?,?)", row)
        except Exception:
            original.unlink(missing_ok=True)
            thumbnail.unlink(missing_ok=True)
            raise
        return {
            "id": sid,
            "model_status": "not_configured",
            "message": "Photo saved. Disease analysis will be available after a trained model is connected.",
        }

    @app.get("/api/scans")
    def scans(limit: int = Query(30, ge=1, le=100), offset: int = Query(0, ge=0)):
        with connection() as c:
            total = c.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
            rows = c.execute(
                "SELECT * FROM scans ORDER BY uploaded DESC,id DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()
        return {
            "total": total,
            "items": [
                {
                    **dict(r),
                    "context": json.loads(r["context"]),
                    "preview_url": "/api/scans/" + r["id"] + "/image",
                    "model_status": "not_configured",
                }
                for r in rows
            ],
        }

    @app.get("/api/scans/{sid}/image")
    def scan_image(sid: str):
        if len(sid) != 32 or any(c not in "0123456789abcdef" for c in sid):
            raise HTTPException(404)
        with connection() as c:
            r = c.execute("SELECT id FROM scans WHERE id=?", (sid,)).fetchone()
        if not r:
            raise HTTPException(404)
        return FileResponse(uploads / (sid + ".jpg"), media_type="image/jpeg")

    @app.get("/api/export/telemetry.csv")
    def export(source: Source = "simulated"):
        def generate():
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(
                [
                    "id",
                    "node",
                    "zone",
                    "source",
                    "captured_at",
                    "received_at",
                    "temperature_c",
                    "humidity_pct",
                    "soil_relative_pct",
                    "soil_raw_adc",
                    "leaf_wetness_raw",
                    "leaf_wetness_state",
                    "light_lux",
                    "calibration_id",
                    "boot_id",
                    "sequence",
                ]
            )
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)
            with connection() as c:
                for row in c.execute(
                    "SELECT * FROM telemetry WHERE source=? ORDER BY captured,id",
                    (source,),
                ):
                    r = json.loads(row["payload"])
                    m = r["measurements"]
                    values = [
                        row["id"],
                        r["node_id"],
                        r["zone_id"],
                        r["source_type"],
                        r["captured_at"],
                        row["received"],
                        m["air_temperature_c"],
                        m["relative_humidity_pct"],
                        m["soil_moisture_relative_pct"],
                        m["soil_moisture_raw_adc"],
                        m["leaf_wetness_raw"],
                        m["leaf_wetness_state"],
                        m["light_lux"],
                        r["calibration_id"],
                        r["boot_id"],
                        r["sequence"],
                    ]
                    writer.writerow(
                        [
                            "'" + v
                            if isinstance(v, str)
                            and v.startswith(("=", "+", "-", "@", "\t", "\r"))
                            else v
                            for v in values
                        ]
                    )
                    yield output.getvalue()
                    output.seek(0)
                    output.truncate(0)

        return StreamingResponse(
            generate(),
            media_type="text/csv",
            headers={
                "Content-Disposition": f'attachment; filename="plantguard-{source}.csv"'
            },
        )

    dist = ROOT / "frontend/dist"
    if dist.exists():
        app.mount("/", StaticFiles(directory=dist, html=True), name="dashboard")
    return app
