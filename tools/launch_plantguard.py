"""Start/stop PlantGuard on this laptop. Does not install software or send data online."""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = ROOT / ".venv/Scripts/python.exe"
RUNTIME = ROOT / "runtime"
URL = "http://127.0.0.1:8765"
PIDFILE = RUNTIME / "server.pid"
HIDDEN = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def health():
    try:
        with urllib.request.urlopen(URL + "/api/health", timeout=2) as response:
            value = json.load(response)
        return value if value.get("application") == "PlantGuard" else None
    except Exception:
        return None


def stop():
    if not PIDFILE.exists():
        print("No launcher-managed server PID was found.")
        return
    pid = int(PIDFILE.read_text(encoding="utf-8-sig").strip())
    command = f"Get-CimInstance Win32_Process -Filter 'ProcessId = {pid}' | Select-Object ExecutablePath,CommandLine | ConvertTo-Json -Compress"
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        creationflags=HIDDEN,
        check=True,
    )
    if not result.stdout.strip():
        PIDFILE.unlink()
        print("PlantGuard is already stopped.")
        return
    process = json.loads(result.stdout)
    executable = process.get("ExecutablePath") or ""
    arguments = process.get("CommandLine") or ""
    if (
        Path(executable).resolve() != PYTHON.resolve()
        or "backend.app:create_app" not in arguments
        or "8765" not in arguments
    ):
        raise RuntimeError(
            "The saved PID belongs to a different process. It was left running."
        )
    os.kill(pid, 15)
    PIDFILE.unlink(missing_ok=True)
    print("PlantGuard stopped. Photos and readings are retained in runtime.")


def start(open_browser=True):
    RUNTIME.mkdir(exist_ok=True)
    if not PYTHON.is_file():
        raise RuntimeError(
            "Python environment missing. Follow docs/Phase_3_2026-09-13/README.md."
        )
    if not (ROOT / "frontend/dist/index.html").is_file():
        raise RuntimeError(
            "Dashboard build missing. Run npm --prefix frontend run build from the project folder."
        )
    if not health():
        with (
            (RUNTIME / "server.stdout.log").open("ab") as output,
            (RUNTIME / "server.stderr.log").open("ab") as errors,
        ):
            server = subprocess.Popen(
                [
                    str(PYTHON),
                    "-m",
                    "uvicorn",
                    "backend.app:create_app",
                    "--factory",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    "8765",
                ],
                cwd=ROOT,
                stdout=output,
                stderr=errors,
                creationflags=HIDDEN,
            )
        for _ in range(40):
            if server.poll() is not None:
                raise RuntimeError(
                    "Server did not start. Check runtime/server.stderr.log (port 8765 may be occupied)."
                )
            if health():
                PIDFILE.write_text(str(server.pid), encoding="utf-8")
                break
            time.sleep(0.5)
        else:
            server.terminate()
            raise RuntimeError(
                "Server startup timed out. Check runtime/server.stderr.log."
            )
    print("PlantGuard is running at " + URL)
    print(
        "Use Stop_PlantGuard.cmd when finished. Closing the browser does not stop the server."
    )
    if open_browser:
        webbrowser.open(URL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stop", action="store_true")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    try:
        stop() if args.stop else start(not args.no_browser)
    except Exception as error:
        print("PlantGuard: " + str(error))
        sys.exit(1)
