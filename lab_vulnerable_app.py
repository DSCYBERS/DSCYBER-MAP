#!/usr/bin/env python3
"""Local intentionally-vulnerable lab server (SAFE: localhost only).

This is for authorized testing demos.
It simulates SQL errors when common injection characters/patterns appear.

Run:
  python lab_vulnerable_app.py
Then test with the framework against:
  http://127.0.0.1:8001/listproducts.php?cat=1
"""

from __future__ import annotations

import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

HOST = "127.0.0.1"
PORT = 8001

_SQLI_PATTERNS = [
    r"'",
    r"\"",
    r"--",
    r"/\*",
    r"\*/",
    r"\bor\b\s+1\s*=\s*1\b",
    r"\bunion\b\s+\bselect\b",
    r"\bsleep\s*\(",
    r"\bwaitfor\b\s+\bdelay\b",
]
_SQLI_RE = re.compile("|".join(_SQLI_PATTERNS), re.IGNORECASE)


def _looks_like_sqli(value: str) -> bool:
    return bool(_SQLI_RE.search(value or ""))


class LabHandler(BaseHTTPRequestHandler):
    server_version = "DSCYBER-Lab/1.0"

    def log_message(self, fmt: str, *args):
        # quieter console output
        return

    def _send(self, status: int, body: str, content_type: str = "text/html; charset=utf-8"):
        body_bytes = body.encode("utf-8", errors="replace")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body_bytes)))
        self.end_headers()
        self.wfile.write(body_bytes)

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        # A demo endpoint that mimics a vulnerable parameter
        if parsed.path in ("/", "/listproducts.php", "/listproducts.php/"):
            cat = (qs.get("cat") or [""])[0]
            if _looks_like_sqli(cat):
                # Simulated SQL error signature
                self._send(
                    500,
                    """<html><body>
<h1>Database Error</h1>
<p>You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1</p>
</body></html>""",
                )
                return

            self._send(
                200,
                f"""<html><body>
<h1>Products</h1>
<p>Category: {cat or '1'}</p>
</body></html>""",
            )
            return

        if parsed.path == "/health":
            self._send(200, json.dumps({"ok": True}), "application/json; charset=utf-8")
            return

        self._send(404, "<html><body><h1>404</h1></body></html>")

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length) if length > 0 else b""
        body = raw.decode("utf-8", errors="replace")

        # A demo login endpoint that simulates SQLi on user/pass
        if parsed.path in ("/login", "/login/"):
            # naive parse: user=...&pass=...
            params = parse_qs(body)
            user = (params.get("user") or [""])[0]
            password = (params.get("pass") or [""])[0]

            if _looks_like_sqli(user) or _looks_like_sqli(password):
                self._send(
                    500,
                    """<html><body>
<h1>Database Error</h1>
<pre>SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax</pre>
</body></html>""",
                )
                return

            self._send(200, "<html><body><h1>Login</h1><p>Invalid credentials</p></body></html>")
            return

        self._send(404, "<html><body><h1>404</h1></body></html>")


def main():
    httpd = HTTPServer((HOST, PORT), LabHandler)
    print(f"[DSCYBER-LAB] Running on http://{HOST}:{PORT}")
    print("[DSCYBER-LAB] Demo target: /listproducts.php?cat=1")
    print("[DSCYBER-LAB] Demo login:  POST /login with user=...&pass=...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
