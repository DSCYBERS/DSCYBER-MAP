#!/usr/bin/env python3
"""Auto-configure DSCYBER with target"""

import json
from pathlib import Path
import socket

# Configuration
target_url = "http://testphp.vulnweb.com/"

# Parse target
from urllib.parse import urlparse

parsed = urlparse(target_url)
target_host = parsed.hostname or "testphp.vulnweb.com"
target_port = parsed.port or (443 if parsed.scheme == "https" else 80)

# Session file
framework_dir = Path(__file__).parent
session_file = framework_dir / ".dscyber_session.json"

# Create session
session = {
    "target_url": target_url,
    "target_host": target_host,
    "target_port": target_port,
    "db_type": "MySQL"
}

# Save
with open(session_file, 'w') as f:
    json.dump(session, f, indent=2)

print("✓ Target Configured:")
print(f"  URL:       {target_url}")
print(f"  Host:      {target_host}")
print(f"  Port:      {target_port}")
print(f"  DB Type:   MySQL")
print()
print("✓ Session saved to .dscyber_session.json")
print()
print("Next: Run 'python dscyber.py' and press [C] to confirm target")
