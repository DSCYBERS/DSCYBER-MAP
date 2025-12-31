#!/usr/bin/env python3
"""
DSCYBER Auto-Attack Script
Confirms target and runs AUTO mode automatically
"""

import subprocess
import sys
import time

# Input sequence to run AUTO mode attack
# C = Confirm target
# 1 = Run AUTO mode  
# (let it run)

input_commands = "C\n1\n"

print("\n" + "="*80)
print("DSCYBER v3.0.1 - AUTO ATTACK EXECUTION")
print("="*80)
print("\nTarget: http://testphp.vulnweb.com/")
print("Mode: AUTO (Complete Automatic Exploitation)")
print("Duration: ~3 minutes")
print("\n[*] Starting attack in 2 seconds...\n")
time.sleep(2)

try:
    process = subprocess.Popen(
        [sys.executable, "dscyber.py"],
        stdin=subprocess.PIPE,
        text=True
    )
    
    # Send commands
    process.stdin.write(input_commands)
    process.stdin.flush()
    
    # Let framework run
    process.wait()
    
except KeyboardInterrupt:
    print("\n\n[!] Attack interrupted")
    process.terminate()
except Exception as e:
    print(f"Error: {e}")
