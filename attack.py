#!/usr/bin/env python3
import subprocess

attack_sequence = "0\nhttp://testphp.vulnweb.com/\nC\nyes\n1\n"

process = subprocess.Popen(
    ["python", "dscyber.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding='utf-8',
    errors='replace'
)

stdout, _ = process.communicate(input=attack_sequence)
print(stdout)
