"""Start the local educational appointment-booking demo on port 8000."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent / "demo_app"
os.chdir(ROOT)
print("Demo app running at http://127.0.0.1:8000")
print("Press Ctrl+C to stop.")
ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler).serve_forever()
