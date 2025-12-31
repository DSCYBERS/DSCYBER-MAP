#!/usr/bin/env python3
"""
Automated DSCYBER Attack Runner
Configures target and runs attack mode automatically
"""

import subprocess
import sys
import time

def run_attack():
    """Run DSCYBER with automated target configuration"""
    
    print("\n" + "="*80)
    print("DSCYBER v3.0.1 - AUTOMATED ATTACK EXECUTION")
    print("="*80 + "\n")
    
    # Target configuration
    target_url = "http://testphp.vulnweb.com/"
    
    print(f"[*] Target: {target_url}")
    print(f"[*] Mode: AUTO (Complete automatic exploitation)")
    print(f"[*] Duration: ~3 minutes\n")
    
    # Prepare input sequence:
    # 0 = Configure target
    # (URL input)
    # C = Confirm target
    # yes = Answer yes to confirmation prompt
    # 1 = AUTO mode
    # X = Exit
    
    input_sequence = f"0\n{target_url}\nC\nyes\n1\nX\n"
    
    print("[*] Starting DSCYBER framework...\n")
    time.sleep(1)
    
    try:
        # Run dscyber.py with input
        process = subprocess.Popen(
            [sys.executable, "dscyber.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding='utf-8',
            errors='replace'
        )
        
        # Send input and get output
        stdout, _ = process.communicate(input=input_sequence, timeout=300)
        
        # Print output
        if stdout:
            print(stdout)
        
        print("\n" + "="*80)
        print("ATTACK EXECUTION COMPLETE")
        print("="*80 + "\n")
        
    except subprocess.TimeoutExpired:
        print("[!] Attack timeout - exceeded 5 minutes")
        process.kill()
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted by user")
        process.kill()
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    run_attack()
