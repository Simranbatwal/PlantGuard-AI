import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import {
  Leaf,
  LayoutDashboard,
  ScanLine,
  FlaskConical,
  ArrowUpRight,
  Download,
  Radio,
  Thermometer,
  Droplets,
  Sun,
  Camera,
  Play,
  Pause,
  AlertCircle,
  Upload,
  Database,
  Clock,
  ShieldCheck,
  Sprout,
  X,
} from "lucide-react";
import "./style.css";
const fmt = (v) =>
  v == null
    ? "—"
    : Number(v).toLocaleString(undefined, { maximumFractionDigits: 1 });
const time = (v) =>
  v
    ? new Date(v).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      })
    : "No reading yet";
const stamp = (v) => (v ? new Date(v).toLocaleString() : "Not available");
const statusNames = {
  current: "Current",
  no_data: "No readings",
  stale: "Stale reading",
  offline: "No recent contact",
  missing: "Measurements missing",
};
const metrics = {
  soil_moisture_relative_pct: ["Soil moisture", "%"],
  relative_humidity_pct: ["Humidity", "%"],
  air_temperature_c: ["Temperature", "°C"],
};
async function api(path, options = {}) {
  const r = await fetch("/api" + path, options);
  const j = await r.json();
  if (!r.ok)
    throw Error(
      typeof j.detail === "string"
        ? j.detail
        : Array.isArray(j.detail)
          ? j.detail.map((x) => x.loc.at(-1) + ": " + x.msg).join("; ")
          : "Request failed. Please try again.",
    );
  return j;
}
function Chart({ rows, metric }) {
  const vals = rows.map((r) => r.measurements[metric]).filter((v) => v != null);
  if (!vals.length)
    return (
      <div className="empty chartempty">
        <Sprout size={34} />
        <h3>A little data goes a long way.</h3>
        <p>
          Start the simulator to see readings here.
          <br />
          Physical readings will appear after hardware is connected.
        </p>
      </div>
    );
  const lo = Math.floor(Math.min(...vals) - 3),
    hi = Math.ceil(Math.max(...vals) + 3),
    start = new Date(rows[0].captured_at).getTime(),
    end = new Date(rows.at(-1).captured_at).getTime();
  const x = (r) =>
      52 +
      ((new Date(r.captured_at).getTime() - start) / Math.max(1, end - start)) *
        668,
    y = (v) => 186 - ((v - lo) / (hi - lo)) * 146;
  let segments = [],
    segment = [];
  for (const r of rows) {
    const v = r.measurements[metric];
    if (v == null) {
      if (segment.length) segments.push(segment);
      segment = [];
    } else segment.push([x(r), y(v)]);
  }
  if (segment.length) segments.push(segment);
  return (
    <div className="chart">
      <svg
        viewBox="0 0 760 230"
        role="img"
        aria-label={
          metrics[metric][0] + " over time; gaps indicate missing measurements"
        }
      >
        {[0, 1, 2, 3].map((n) => (
          <g key={n}>
            <line
              x1="52"
              x2="725"
              y1={40 + (n * 146) / 3}
              y2={40 + (n * 146) / 3}
              stroke="#e4e9e3"
              strokeDasharray="4 5"
            />
            <text x="40" y={44 + (n * 146) / 3} textAnchor="end">
              {fmt(hi - (n * (hi - lo)) / 3)}
            </text>
          </g>
        ))}
        {segments.map((s, i) => (
          <g key={i}>
            <polyline
              points={s.map((p) => p.join(",")).join(" ")}
              fill="none"
              stroke="#3c7757"
              strokeWidth="3"
            />
            {s.map((p, j) => (
              <circle key={j} cx={p[0]} cy={p[1]} r="3.5" fill="#3c7757" />
            ))}
          </g>
        ))}
        <text x="52" y="215">
          {time(rows[0].captured_at)}
        </text>
        <text x="720" y="215" textAnchor="end">
          {time(rows.at(-1).captured_at)}
        </text>
      </svg>
      <div className="chartlegend">
        <span className="dot" />
        {metrics[metric][0]} ({metrics[metric][1]}){" "}
        <span>• {rows.length} latest records • gaps = missing values</span>
      </div>
    </div>
  );
}
function App() {
  const [page, setPage] = useState("overview"),
    [source, setSource] = useState("simulated"),
    [zone, setZone] = useState("A"),
    [metric, setMetric] = useState("soil_moisture_relative_pct"),
    [tick, setTick] = useState(0),
    [data, setData] = useState(null),
    [history, setHistory] = useState([]),
    [scans, setScans] = useState({ items: [], total: 0 }),
    [online, setOnline] = useState(false),
    [loaded, setLoaded] = useState(false),
    [notice, setNotice] = useState(null),
    [busy, setBusy] = useState(false),
    [file, setFile] = useState(null),
    [preview, setPreview] = useState(null),
    [selected, setSelected] = useState(null),
    [scanOffset, setScanOffset] = useState(0),
    [scenario, setScenario] = useState("sample");
  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [page]);
  useEffect(() => {
    let active = true;
    const ctrl = new AbortController();
    Promise.all([
      api("/overview?source=" + source, { signal: ctrl.signal }),
      api("/history?zone=" + zone + "&source=" + source, {
        signal: ctrl.signal,
      }),
      api("/scans?offset=" + scanOffset, { signal: ctrl.signal }),
    ])
      .then(([a, b, c]) => {
        if (active) {
          setData(a);
          setHistory(b);
          setScans(c);
          setOnline(true);
          setLoaded(true);
        }
      })
      .catch((e) => {
        if (active && e.name !== "AbortError") {
          setOnline(false);
          setLoaded(true);
        }
      });
    return () => {
      active = false;
      ctrl.abort();
    };
  }, [source, zone, tick, scanOffset]);
  useEffect(() => {
    const id = setInterval(() => setTick((t) => t + 1), 5000);
    return () => clearInterval(id);
  }, []);
  useEffect(() => {
    if (!file) {
      setPreview(null);
      return;
    }
    const url = URL.createObjectURL(file);
    setPreview(url);
    return () => URL.revokeObjectURL(url);
  }, [file]);
  const matching = data?.source === source,
    zones = matching ? data.zones : [],
    activeZone = zones.find((z) => z.zone_id === zone),
    m = activeZone?.latest?.measurements || {},
    rows = matching
      ? history.filter((r) => r.zone_id === zone && r.source_type === source)
      : [],
    sim = data?.simulator;
  async function action(a) {
    setBusy(true);
    try {
      const r = await api("/simulator", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: a, zone }),
      });
      setNotice({ text: r.message });
      setTick((t) => t + 1);
    } catch (e) {
      setNotice({ text: e.message, error: true });
    } finally {
      setBusy(false);
    }
  }
  function choose(f) {
    if (!f) return;
    if (f.size > 8 * 1024 * 1024) {
      setNotice({ text: "Choose a photo smaller than 8 MiB.", error: true });
      return;
    }
    setFile(f);
  }
  async function save(e) {
    e.preventDefault();
    if (!file) return;
    setBusy(true);
    const form = new FormData();
    form.append("file", file);
    form.append("zone", zone);
    form.append("source", source);
    try {
      const r = await api("/scans", { method: "POST", body: form });
      setNotice({ text: r.message });
      setFile(null);
      setScanOffset(0);
      setTick((t) => t + 1);
    } catch (e) {
      setNotice({ text: e.message, error: true });
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="app">
      <aside className="sidebar">
        <a
          className="brand"
          href="#"
          onClick={(e) => {
            e.preventDefault();
            setPage("overview");
          }}
        >
          <span className="brandmark">
            <Leaf size={26} />
          </span>
          <span>
            PlantGuard<small>PLANT HEALTH WORKSPACE</small>
          </span>
        </a>
        <div className="navlabel">WORKSPACE</div>
        <nav>
          {[
            ["overview", LayoutDashboard, "Overview"],
            ["scans", ScanLine, "Leaf scans"],
            ["lab", FlaskConical, "Demo & testing"],
          ].map(([id, Icon, label]) => (
            <button
              key={id}
              aria-label={label}
              title={label}
              className={page === id ? "active" : ""}
              onClick={() => setPage(id)}
            >
              <Icon size={19} />
              <span>{label}</span>
              {page === id && <i />}
            </button>
          ))}
        </nav>
        <div className="sidebarbottom">
          <div className="growcard">
            <Sprout size={34} />
            <h3>
              Small signals.
              <br />
              Better understanding.
            </h3>
            <p>
              Tomato plant monitoring
              <br />
              College prototype
            </p>
          </div>
          <div className="profile">
            <span className="avatar">SB</span>
            <div>
              Simran Batwal<small>GNDU · M.Tech CSE</small>
            </div>
          </div>
        </div>
      </aside>
      <main>
        <header>
          <span>
            Workspace <span className="slash">/</span>{" "}
            {page === "overview"
              ? "Overview"
              : page === "scans"
                ? "Leaf scans"
                : "Demo & testing"}
          </span>
          <div className="headerstatus">
            <span className={"dot " + (!online ? "muted" : "")} />
            {online
              ? "Laptop connected"
              : loaded
                ? "Server unavailable"
                : "Connecting…"}
            <span className="avatar">SB</span>
          </div>
        </header>
        <div className="content">
          <section className="hero">
            <div>
              <div className="eyebrow">PLANTGUARD / COLLEGE PROTOTYPE</div>
              <h1>
                {page === "overview"
                  ? "Your plants, in focus."
                  : page === "scans"
                    ? "A closer look at every leaf."
                    : "Test the flow. Understand the signals."}
              </h1>
              <p>
                {page === "overview"
                  ? "A clear view of your growing zones, one reading at a time."
                  : page === "scans"
                    ? "Save leaf photos and their monitoring context in one place."
                    : "Check how the application handles everyday data and common faults."}
              </p>
            </div>
            {page !== "scans" && (
              <button className="primary" onClick={() => setPage("scans")}>
                <Camera size={17} /> New leaf scan <ArrowUpRight size={16} />
              </button>
            )}
          </section>
          <div className={"sourcebar " + source}>
            <div>
              <span className="badge">{source.toUpperCase()} DATA</span>
              <span>
                {source === "simulated"
                  ? "Generated for software testing. These are not plant measurements."
                  : source === "physical"
                    ? "Physical source view. Device authentication and hardware validation are pending."
                    : "Replayed records. These are not live measurements."}
              </span>
            </div>
            <label>
              Data source
              <select
                value={source}
                onChange={(e) => setSource(e.target.value)}
              >
                <option value="simulated">Simulator</option>
                <option value="physical">Physical sensors</option>
                <option value="replay">Replay</option>
              </select>
            </label>
          </div>
          {loaded && !online && (
            <div className="notice error" role="alert">
              <AlertCircle size={18} />
              <span>
                Local server is unavailable. Visible readings are cached and may
                be out of date.
              </span>
              <button onClick={() => setTick((t) => t + 1)}>Retry</button>
            </div>
          )}
          {notice && (
            <div
              className={"notice " + (notice.error ? "error" : "")}
              role="status"
            >
              <AlertCircle size={18} />
              <span>{notice.text}</span>
              <button
                aria-label="Dismiss message"
                onClick={() => setNotice(null)}
              >
                <X size={17} />
              </button>
            </div>
          )}
          {page === "overview" && (
            <>
              <section className="stats">
                {[
                  [
                    Radio,
                    "Monitoring zones",
                    "02",
                    "Two independently tracked zones",
                  ],
                  [
                    Database,
                    "Saved readings",
                    matching ? fmt(data.reading_count) : "—",
                    source + " records only",
                  ],
                  [
                    Camera,
                    "Leaf photos",
                    fmt(scans.total),
                    "Across all data sources",
                  ],
                  [
                    ShieldCheck,
                    "Disease model",
                    "Pending",
                    "No trained model connected",
                  ],
                ].map(([Icon, label, value, note]) => (
                  <div className="stat" key={label}>
                    <div className="statlabel">
                      <span>{label}</span>
                      <Icon size={19} />
                    </div>
                    <strong>{value}</strong>
                    <small>{note}</small>
                  </div>
                ))}
              </section>
              <div className="sectiontitle">
                <h2>Growing zones</h2>
                <span>Select a zone to explore its readings</span>
              </div>
              <section className="zones">
                {["A", "B"].map((id) => {
                  const z = zones.find((x) => x.zone_id === id),
                    v = z?.latest?.measurements || {};
                  return (
                    <button
                      key={id}
                      className={"zonecard " + (zone === id ? "selected" : "")}
                      onClick={() => setZone(id)}
                    >
                      <div className="zonehead">
                        <span className="planticon">
                          <Sprout size={24} />
                        </span>
                        <div>
                          <h3>Zone {id}</h3>
                          <p>Tomato · Sensor node PG-{id}</p>
                        </div>
                        <span
                          className={
                            "status " + (online ? z?.status : "offline")
                          }
                        >
                          {online
                            ? statusNames[z?.status] || "Loading…"
                            : "Unavailable"}
                        </span>
                      </div>
                      <div className="zonemetrics">
                        <div>
                          <Thermometer size={16} />
                          <strong>
                            {fmt(v.air_temperature_c)}
                            <small> °C</small>
                          </strong>
                          <span>Air temperature</span>
                        </div>
                        <div>
                          <Droplets size={16} />
                          <strong>
                            {fmt(v.relative_humidity_pct)}
                            <small> %</small>
                          </strong>
                          <span>Humidity</span>
                        </div>
                        <div>
                          <Leaf size={16} />
                          <strong>
                            {fmt(v.soil_moisture_relative_pct)}
                            <small> %</small>
                          </strong>
                          <span>Relative soil moisture</span>
                        </div>
                      </div>
                      <div className="zonefoot">
                        <span>
                          <Clock size={13} /> {time(z?.latest?.captured_at)}
                        </span>
                        <span>
                          {zone === id ? "Viewing zone" : "View readings"}{" "}
                          <ArrowUpRight size={13} />
                        </span>
                      </div>
                    </button>
                  );
                })}
              </section>
              <section className="analysisgrid">
                <div className="panel">
                  <div className="panelhead">
                    <div>
                      <h2>Reading trends</h2>
                      <p>Zone {zone} · capture time</p>
                    </div>
                    <select
                      aria-label="Chart measurement"
                      value={metric}
                      onChange={(e) => setMetric(e.target.value)}
                    >
                      {Object.entries(metrics).map(([k, v]) => (
                        <option key={k} value={k}>
                          {v[0]}
                        </option>
                      ))}
                    </select>
                  </div>
                  <Chart rows={rows} metric={metric} />
                </div>
                <div className="panel snapshot">
                  <div className="panelhead">
                    <div>
                      <h2>Zone {zone} snapshot</h2>
                      <p>Latest monitoring context</p>
                    </div>
                    <Leaf size={20} />
                  </div>
                  <div className="snapshotrow">
                    <span>
                      <Droplets size={17} /> Leaf wetness
                    </span>
                    <strong>{m.leaf_wetness_state || "—"}</strong>
                  </div>
                  <div className="snapshotrow">
                    <span>
                      <Sun size={17} /> Light
                    </span>
                    <strong>{fmt(m.light_lux)} lux</strong>
                  </div>
                  <div className="snapshotrow">
                    <span>
                      <Radio size={17} /> Last contact
                    </span>
                    <strong>{time(activeZone?.last_contact)}</strong>
                  </div>
                  <div className="notebox">
                    <ShieldCheck size={20} />
                    <p>
                      Environmental readings describe growing conditions. They
                      do not confirm a disease.
                    </p>
                  </div>
                </div>
              </section>
              <div className="panel readings">
                <div className="panelhead">
                  <div>
                    <h2>Recent readings</h2>
                    <p>Zone {zone} · latest six records</p>
                  </div>
                  <a
                    className="secondary"
                    href={"/api/export/telemetry.csv?source=" + source}
                  >
                    <Download size={15} /> Export {source} CSV
                  </a>
                </div>
                <div className="tablewrap">
                  <table>
                    <thead>
                      <tr>
                        <th>Capture time</th>
                        <th>Source</th>
                        <th>Temperature</th>
                        <th>Humidity</th>
                        <th>Soil raw ADC</th>
                        <th>Leaf wetness</th>
                      </tr>
                    </thead>
                    <tbody>
                      {rows
                        .slice(-6)
                        .reverse()
                        .map((r) => (
                          <tr key={r.id}>
                            <td>{stamp(r.captured_at)}</td>
                            <td>
                              <span className="tinybadge">{r.source_type}</span>
                            </td>
                            <td>{fmt(r.measurements.air_temperature_c)} °C</td>
                            <td>
                              {fmt(r.measurements.relative_humidity_pct)} %
                            </td>
                            <td>{fmt(r.measurements.soil_moisture_raw_adc)}</td>
                            <td>{r.measurements.leaf_wetness_state}</td>
                          </tr>
                        ))}
                      {!rows.length && (
                        <tr>
                          <td colSpan="6" className="emptycell">
                            No readings for this source and zone yet.
                          </td>
                        </tr>
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          )}
          {page === "scans" && (
            <>
              <section className="scangrid">
                <form className="panel" onSubmit={save}>
                  <div className="panelhead">
                    <div>
                      <h2>Upload a leaf photo</h2>
                      <p>
                        JPEG, PNG or WebP · up to 8 MiB · minimum 64 × 64 px
                      </p>
                    </div>
                    <Camera size={20} />
                  </div>
                  <label
                    className={"dropzone " + (preview ? "haspreview" : "")}
                    onDragOver={(e) => e.preventDefault()}
                    onDrop={(e) => {
                      e.preventDefault();
                      choose(e.dataTransfer.files[0]);
                    }}
                  >
                    <input
                      type="file"
                      aria-label="Choose leaf photo"
                      accept="image/jpeg,image/png,image/webp"
                      onChange={(e) => {
                        choose(e.target.files[0]);
                        e.target.value = "";
                      }}
                    />
                    {preview ? (
                      <img src={preview} alt="Selected leaf photo preview" />
                    ) : (
                      <>
                        <span className="uploadicon">
                          <Upload size={26} />
                        </span>
                        <h3>Drop a photo here</h3>
                        <p>or click to browse your files</p>
                        <span className="secondary">Choose photo</span>
                      </>
                    )}
                  </label>
                  {file && (
                    <div className="filename">
                      <span>{file.name}</span>
                      <button
                        type="button"
                        onClick={() => setFile(null)}
                        aria-label="Remove selected photo"
                      >
                        <X size={17} />
                      </button>
                    </div>
                  )}
                  <div className="uploadcontrols">
                    <label>
                      Associate with
                      <select
                        aria-label="Photo zone"
                        value={zone}
                        onChange={(e) => setZone(e.target.value)}
                      >
                        <option value="A">Zone A · Tomato</option>
                        <option value="B">Zone B · Tomato</option>
                      </select>
                    </label>
                    <button
                      type="submit"
                      className="primary"
                      disabled={!file || busy || !online}
                    >
                      <Upload size={16} />
                      {busy ? "Saving…" : "Save leaf photo"}
                    </button>
                  </div>
                  <p className="fineprint">
                    Monitoring context: {source}. The latest reading is attached
                    at upload time; the photo's capture time is unknown. This is
                    not a paired training sample.
                  </p>
                </form>
                <div className="modelcard">
                  <span className="modelicon">
                    <ScanLine size={36} />
                  </span>
                  <span className="badge">MODEL NOT CONFIGURED</span>
                  <h2>
                    Disease analysis
                    <br />
                    comes next.
                  </h2>
                  <p>
                    Photos can be saved now. Disease labels and confidence
                    scores will appear after a trained model is connected and
                    checked.
                  </p>
                  <div className="modelsteps">
                    <div>
                      <span>01</span> Save photos & monitoring context
                    </div>
                    <div>
                      <span>02</span> Train and compare four models
                    </div>
                    <div>
                      <span>03</span> Connect the selected model
                    </div>
                  </div>
                  <small>Current output: saved photo, not a diagnosis.</small>
                </div>
              </section>
              <div className="sectiontitle">
                <h2>
                  Photo library <span className="count">{scans.total}</span>
                </h2>
                <span>All sources · newest uploads first</span>
              </div>
              {!scans.items.length ? (
                <div className="panel empty libraryempty">
                  <Camera size={32} />
                  <h3>Your first leaf photo starts here.</h3>
                  <p>
                    Saved photos will appear here with their zone and source.
                  </p>
                </div>
              ) : (
                <section className="photogrid">
                  {scans.items.map((s) => (
                    <div className="photocard" key={s.id}>
                      <button
                        className="photoopen"
                        onClick={() =>
                          setSelected(selected === s.id ? null : s.id)
                        }
                        aria-label={"View details for " + s.filename}
                      >
                        <img
                          src={s.preview_url}
                          alt={"Saved photo for zone " + s.zone}
                        />
                      </button>
                      <div className="photoinfo">
                        <div>
                          <h3>Zone {s.zone}</h3>
                          <span className="tinybadge">{s.source}</span>
                        </div>
                        <p>{stamp(s.uploaded)}</p>
                        <span className="pending">Analysis pending</span>
                        {selected === s.id && (
                          <div className="photodetail">
                            <strong>{s.filename}</strong>
                            <p>
                              {s.width} × {s.height} px · {s.format}
                            </p>
                            <p>{s.context.association}</p>
                            <p>
                              Context reading:{" "}
                              {s.context.reading
                                ? stamp(s.context.reading.captured_at)
                                : "None available"}
                            </p>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </section>
              )}
              {scans.total > 30 && (
                <div className="pagination">
                  <button
                    className="secondary"
                    disabled={scanOffset === 0}
                    onClick={() => setScanOffset(Math.max(0, scanOffset - 30))}
                  >
                    Previous
                  </button>
                  <span>
                    {scanOffset + 1}–{Math.min(scanOffset + 30, scans.total)} of{" "}
                    {scans.total}
                  </span>
                  <button
                    className="secondary"
                    disabled={scanOffset + 30 >= scans.total}
                    onClick={() => setScanOffset(scanOffset + 30)}
                  >
                    Next
                  </button>
                </div>
              )}
            </>
          )}
          {page === "lab" && (
            <>
              <section className="testintro panel">
                <FlaskConical size={32} />
                <div>
                  <h2>A safe place to test the software.</h2>
                  <p>
                    These scenarios write only to simulated history. Stop
                    automatic simulation before inspecting missing or delayed
                    samples. A delayed packet stays in history and does not
                    replace a newer reading.
                  </p>
                </div>
              </section>
              <section className="testgrid">
                {[
                  [
                    "sample",
                    "Normal sample",
                    "Saves one valid reading for the selected zone.",
                    "A new record appears.",
                  ],
                  [
                    "missing",
                    "Missing measurements",
                    "Sends a message with no sensor values.",
                    "The application shows missing values, not zero.",
                  ],
                  [
                    "stale",
                    "Delayed packet",
                    "Sends a reading captured ten minutes ago.",
                    "Old data cannot overwrite newer data.",
                  ],
                  [
                    "duplicate",
                    "Duplicate message",
                    "Resends the same message identity and payload.",
                    "The saved record count does not increase.",
                  ],
                  [
                    "invalid",
                    "Invalid humidity",
                    "Tries a humidity value of 150%.",
                    "Validation rejects it before storage.",
                  ],
                  [
                    "disconnect",
                    "Pause one zone",
                    "Pauses automatic messages for one zone.",
                    "No recent contact appears after 180 seconds.",
                  ],
                ].map(([a, t, d, e], i) => (
                  <div className="panel testcard" key={a}>
                    <span className="testnumber">0{i + 1}</span>
                    <h3>{t}</h3>
                    <p>{d}</p>
                    <small>{e}</small>
                    <button
                      className="secondary"
                      disabled={busy || !online}
                      onClick={() => action(a)}
                    >
                      Run for zone {zone}
                      <ArrowUpRight size={15} />
                    </button>
                  </div>
                ))}
              </section>
            </>
          )}
          <section className="panel simulator">
            <div className="simtop">
              <div className="simheading">
                <span className="simicon">
                  <FlaskConical size={22} />
                </span>
                <div>
                  <h2>Sensor simulator</h2>
                  <p>Software testing · generated inputs only</p>
                </div>
                <span className={"status " + (sim?.running ? "current" : "")}>
                  {sim?.running ? "Running" : "Stopped"}
                </span>
              </div>
              <button
                className={sim?.running ? "secondary" : "primary"}
                disabled={busy || !online}
                onClick={() => action(sim?.running ? "stop" : "start")}
              >
                {sim?.running ? <Pause size={15} /> : <Play size={15} />}{" "}
                {sim?.running ? "Stop simulator" : "Start simulator"}
              </button>
            </div>
            <div className="simcontrols">
              <label>
                Zone
                <select
                  aria-label="Simulator zone"
                  value={zone}
                  onChange={(e) => setZone(e.target.value)}
                >
                  <option value="A">Zone A</option>
                  <option value="B">Zone B</option>
                </select>
              </label>
              <label>
                Scenario
                <select
                  aria-label="Simulator scenario"
                  value={scenario}
                  onChange={(e) => setScenario(e.target.value)}
                >
                  {[
                    ["sample", "Normal sample"],
                    ["missing", "Missing measurements"],
                    ["stale", "Delayed packet (10 min old)"],
                    ["duplicate", "Duplicate message"],
                    ["invalid", "Invalid humidity (150%)"],
                    ["disconnect", "Pause zone"],
                    ["reconnect", "Enable zone"],
                  ].map(([v, t]) => (
                    <option key={v} value={v}>
                      {t}
                    </option>
                  ))}
                </select>
              </label>
              <button
                className="secondary"
                disabled={busy || !online}
                onClick={() => action(scenario)}
              >
                Run test
                <ArrowUpRight size={15} />
              </button>
              <div className="zoneenabled">
                {["A", "B"].map((z) => (
                  <span key={z}>
                    <span
                      className={"dot " + (sim?.enabled[z] ? "" : "muted")}
                    />
                    Zone {z}: {sim?.enabled[z] ? "enabled" : "paused"}
                  </span>
                ))}
              </div>
            </div>
            <p className="fineprint">
              Automatic samples arrive every 10 seconds. Readings become stale
              or offline after 180 seconds. Pause/stop keeps saved history.{" "}
              {sim?.error}
            </p>
          </section>
          <footer>
            <span>
              <Leaf size={14} /> PlantGuard · Monitor. Understand. Grow.
            </span>
            <span>Stored on this laptop · College prototype · v0.3.0</span>
          </footer>
        </div>
      </main>
    </div>
  );
}
createRoot(document.getElementById("root")).render(<App />);
