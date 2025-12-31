# ██████ DSCYBER‑MAP ██████
_Operator Manual — Offensive‑Defense Intelligence Framework_

  Advanced attack-surface mapping, autonomous offensive automation, pivoting, and AI-driven threat correlation.
  Built for operators, researchers, and blue teams who think like attackers — and defend like pros.

────────────────────────────────────────────────────────────────────────────
WARNING — Read Before Running
────────────────────────────────────────────────────────────────────────────
This framework contains offensive capabilities and powerful automation. Do NOT run DSCYBER‑MAP
against networks, systems, or services you do not own or have explicit written authorization
to test. Use only in isolated lab environments, VMs, or sanctioned red‑team engagements.

By using this repository you agree to follow all local laws, organizational policies,
and responsible disclosure practices. See OPSEC_AND_ROE.md for Rules of Engagement and
Responsible Use guidance.
────────────────────────────────────────────────────────────────────────────

Quick operator summary
- Clone → prepare environment → fire up lab target → run attack scenario → observe dashboard.
- Core intent: simulate real-world attack paths, chain exploits, pivot, and evaluate SOC responses.
- Audience: red team operators, security researchers, advanced blue teams, CTF authors.

Operator mindset: map everything, assume nothing, automate the grind, watch the map.

────────────────────────────────────────────────────────────────────────────
Operator Quick Start (TL;DR)
────────────────────────────────────────────────────────────────────────────
# Clone
git clone https://github.com/DSCYBERS/DSCYBER-MAP.git
cd DSCYBER-MAP

# Setup (Python 3.10+ recommended)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Initialize config (creates skeleton)
python autoconfig.py --init

# Terminal A: start the vulnerable lab
python lab_vulnerable_app.py

# Terminal B: start real-time dashboard
python elite_real_time_dashboard.py --port 8081

# Terminal C: run a quick attack scenario against the lab
python run_attack.py --input attack_input.txt --target http://127.0.0.1:8080 --mode quick

Open: http://127.0.0.1:8081 — watch assets, attack graph, timelines.

────────────────────────────────────────────────────────────────────────────
Operator Playbook (what to run when)
────────────────────────────────────────────────────────────────────────────
- Recon & Map
  -> data_intelligence_analyzer.py
  Purpose: ingest scans, build asset graph, and score exposure.

- Strike (single-target / quick)
  -> run_attack.py / attack_input.txt
  Purpose: reproduce a short scenario to validate detection & response.

- Automate & Pivot
  -> auto_pivoting_engine.py
  Purpose: chain access, route traffic, simulate lateral movement.

- Post-Exploit Automation
  -> post_exploitation_automation.py
  Purpose: persistence, data collection, simulated exfiltrations.

- Visual Ops
  -> elite_real_time_dashboard.py
  Purpose: visualize attack paths, timelines, and defender alerts.

- Defensive Test
  -> threat_detection_monitor.py
  Purpose: monitor for simulated IOCs and SOC responses.

────────────────────────────────────────────────────────────────────────────
Modules (fast reference)
────────────────────────────────────────────────────────────────────────────
- dscyber.py               — orchestrator
- data_intelligence_analyzer.py — mapping & AI correlation
- auto_pivoting_engine.py  — pivot / lateral engine
- post_exploitation_automation.py — post-exploit suites
- sqlmap_interactive_tool.py / advanced_database_dumper.py — DB helpers
- lab_vulnerable_app.py    — built-in training target
- run_attack.py / auto_attack.py — scenario runners
- elite_real_time_dashboard.py — real-time visualization

────────────────────────────────────────────────────────────────────────────
Hacker Notes & Modes (terminology)
────────────────────────────────────────────────────────────────────────────
- quick — short scenario, minimal noise, demo-focused
- stealth — lower-noise simulation to test detection thresholds (use with caution)
- noisy — aggressive scans and multiple exploit chains (lab-only)
- ctf — contest mode (use lab_vulnerable_app.py with custom challenges)

Always annotate your runs: include run-id, mission tag, and start/end times in logs.

────────────────────────────────────────────────────────────────────────────
Operator Tips (safe & effective)
────────────────────────────────────────────────────────────────────────────
- Use the built-in lab_vulnerable_app.py for training and regression.
- Use autoconfig.py to create config skeletons; never commit secrets.
- Tail logs and dashboard for attack graphs — the visualization reveals pivot chains.
- Run dashboard and attack in separate terminals/containers for reproducibility.

────────────────────────────────────────────────────────────────────────────
OPSEC & Rules of Engagement
────────────────────────────────────────────────────────────────────────────
See OPSEC_AND_ROE.md. Highlights:
- Always have written permission.
- Test only in isolated or authorized ranges.
- Preserve logs and notes for after‑action reviews.
- If you find a vulnerability outside the lab, follow responsible disclosure.

────────────────────────────────────────────────────────────────────────────
How to extend (for operators & devs)
────────────────────────────────────────────────────────────────────────────
- New attack module: create under modules/ with CLI flags `--config`, `--log-level`, `--dry-run`.
- New detection rules: add to threat_detection_monitor.py and add corresponding tests.
- New dashboard widgets: extend elite_real_time_dashboard.py (JS/HTML templates).

────────────────────────────────────────────────────────────────────────────
Contributing (fast)
────────────────────────────────────────────────────────────────────────────
- Fork → branch feat/<name> → tests → PR.
- Use clear commit messages, include scenario outputs, attach dashboard screenshots.
- See CONTRIBUTING.md for full flow.

────────────────────────────────────────────────────────────────────────────
Credits & Contact
────────────────────────────────────────────────────────────────────────────
Maintainer: Kashyap Divyansh (DSCYBERS)  
LinkedIn: https://in.linkedin.com/in/kashyap-divyansh-44a3a424b  
GitHub: https://github.com/dscybers

────────────────────────────────────────────────────────────────────────────
Want this live in the repo?
Say “Yes, open PR” and I’ll create a branch, add these hacker‑style docs, and open a PR.
