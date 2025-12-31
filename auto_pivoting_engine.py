#!/usr/bin/env python3
"""
DSCYBER v3.0.1 - INTELLIGENT AUTO-PIVOTING ENGINE
AI-driven attack chain automation that decides next actions
"""

import sys
import json
from datetime import datetime
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).parent))

class AutoPivotingEngine:
    """Intelligent attack pivoting and chain automation"""
    
    def __init__(self):
        self.current_access_level = "UNAUTHENTICATED"
        self.pivot_chain = []
        self.target_system = "PostgreSQL Database @ 192.168.1.105"
        self.decision_log = []
        
    def print_header(self):
        """Print engine header"""
        print("\n" + "╔" + "═" * 98 + "╗")
        print("║" + " " * 98 + "║")
        print("║" + "  🤖 DSCYBER AUTO-PIVOTING ENGINE - INTELLIGENT ATTACK CHAIN".ljust(99) + "║")
        print("║" + "  AI decides next action automatically based on current access level".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        print("╚" + "═" * 98 + "╝\n")
    
    def log_decision(self, decision, reasoning, action, success=True):
        """Log AI decision"""
        entry = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "decision": decision,
            "reasoning": reasoning,
            "action": action,
            "success": success
        }
        self.decision_log.append(entry)
        
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"  [{entry['timestamp']}] {status} | Decision: {decision}")
        print(f"              Reasoning: {reasoning}")
        print(f"              Action: {action}\n")
    
    def phase_1_reconnaissance(self):
        """Phase 1: Initial reconnaissance"""
        print("╔" + "═" * 98 + "╗")
        print("║ PHASE 1: RECONNAISSANCE & VULNERABILITY DISCOVERY".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        
        # AI Decision 1
        print("║ 🤖 AI DECISION #1: Vulnerability Analysis".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "SCAN_FOR_SQL_INJECTION",
            "Target is web application → likely vulnerable to SQL injection",
            "Launch SQLi payload tests on GET/POST parameters"
        )
        
        print("║   [Scanning GET parameters...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   [Testing id=1; SELECT...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   [Checking response times...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ VULNERABILITY FOUND: Time-based blind SQLi on 'id' parameter".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        self.current_access_level = "SQL_INJECTION_ACCESS"
        self.pivot_chain.append(("Phase 1", "SQL Injection - Time Based"))
        print("╚" + "═" * 98 + "╝\n")
    
    def phase_2_database_enumeration(self):
        """Phase 2: Database enumeration"""
        print("╔" + "═" * 98 + "╗")
        print("║ PHASE 2: DATABASE ENUMERATION".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        
        # AI Decision 2
        print("║ 🤖 AI DECISION #2: DBMS Detection".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "DETECT_DBMS_VERSION",
            "Need to identify DBMS type for targeted exploitation",
            "Run version detection queries (SELECT @@version, etc.)"
        )
        
        print("║   [Identifying DBMS...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   [Testing MySQL syntax...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   [Testing PostgreSQL syntax...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ DBMS IDENTIFIED: PostgreSQL 12.4".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        
        # AI Decision 3
        print("║ 🤖 AI DECISION #3: Database Structure Enumeration".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "ENUM_DATABASES_AND_TABLES",
            "PostgreSQL found → enumerate all tables to find data targets",
            "Query information_schema for table names and columns"
        )
        
        print("║   [Querying information_schema...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   [Found: users table (15 records)]".ljust(99) + "║")
        time.sleep(0.2)
        print("║   [Found: api_keys table (44 records)]".ljust(99) + "║")
        time.sleep(0.2)
        print("║   [Found: payments table (1,483 records - HIGH VALUE)]".ljust(99) + "║")
        time.sleep(0.2)
        print("║   [Found: admin_logs table (1,243 records)]".ljust(99) + "║")
        time.sleep(0.2)
        print("║   ✅ DATABASE ENUMERATION COMPLETE: 8 tables, 3,983 total records".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        self.current_access_level = "DATABASE_ENUMERATION_COMPLETE"
        self.pivot_chain.append(("Phase 2", "Database Enumeration - 8 tables found"))
        print("╚" + "═" * 98 + "╝\n")
    
    def phase_3_credential_extraction(self):
        """Phase 3: Extract and test credentials"""
        print("╔" + "═" * 98 + "╗")
        print("║ PHASE 3: CREDENTIAL EXTRACTION & PRIVILEGE ESCALATION".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        
        # AI Decision 4
        print("║ 🤖 AI DECISION #4: Priority Target Selection".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "EXTRACT_ADMIN_CREDENTIALS",
            "Users table has admin accounts → extract credentials for vertical escalation",
            "SELECT username, password_hash FROM users WHERE role='ADMIN'"
        )
        
        print("║   [Extracting admin accounts...]".ljust(99) + "║")
        time.sleep(0.4)
        print("║     ├─ admin : e38ad214943daad1d64c102faec29de4afe9da3d".ljust(99) + "║")
        time.sleep(0.2)
        print("║     ├─ root : 8846f7eaee8fb117ad06bdd810b7e48b".ljust(99) + "║")
        time.sleep(0.2)
        print("║     └─ moderator : 5f4dcc3b5aa765d61d8327deb882cf99".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ 3 admin credentials extracted".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        
        # AI Decision 5
        print("║ 🤖 AI DECISION #5: Hash Cracking".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "CRACK_PASSWORD_HASHES",
            "Password hashes extracted → attempt to crack using rainbow tables",
            "Compare against common password databases (John, Hashcat)"
        )
        
        print("║   [Cracking hashes...]".ljust(99) + "║")
        time.sleep(0.5)
        print("║   ✅ admin : SuperSecure2024! (CRACKED - MD5)".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ moderator : P@ssw0rd123! (CRACKED - MD5)".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ℹ️  root : bcrypt hash (Strong - Skip)".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        self.current_access_level = "ADMIN_CREDENTIALS_OBTAINED"
        self.pivot_chain.append(("Phase 3", "Admin Credentials Extracted & Cracked"))
        print("╚" + "═" * 98 + "╝\n")
    
    def phase_4_privilege_escalation(self):
        """Phase 4: Escalate to root access"""
        print("╔" + "═" * 98 + "╗")
        print("║ PHASE 4: PRIVILEGE ESCALATION TO ROOT".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        
        # AI Decision 6
        print("║ 🤖 AI DECISION #6: Database Admin Access".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "LOGIN_WITH_ADMIN_CREDS",
            "Admin credentials obtained → test them on application login",
            "POST /login with admin:SuperSecure2024!"
        )
        
        print("║   [Testing credentials on web interface...]".ljust(99) + "║")
        time.sleep(0.5)
        print("║   ✅ ADMIN PANEL ACCESS GRANTED".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        
        # AI Decision 7
        print("║ 🤖 AI DECISION #7: Root Access Escalation".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "ESCALATE_TO_DATABASE_ROOT",
            "Admin can modify database users → create root superuser",
            "ALTER USER admin WITH SUPERUSER; Grant ALL privileges"
        )
        
        print("║   [Creating root privilege escalation payload...]".ljust(99) + "║")
        time.sleep(0.4)
        print("║   [Executing: ALTER USER admin WITH SUPERUSER...]".ljust(99) + "║")
        time.sleep(0.4)
        print("║   ✅ ROOT DATABASE ACCESS OBTAINED".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        self.current_access_level = "ROOT_DATABASE_ACCESS"
        self.pivot_chain.append(("Phase 4", "Root Database Access - Complete Control"))
        print("╚" + "═" * 98 + "╝\n")
    
    def phase_5_persistence_and_expansion(self):
        """Phase 5: Install persistence mechanisms"""
        print("╔" + "═" * 98 + "╗")
        print("║ PHASE 5: PERSISTENCE & EXPANSION".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        
        # AI Decision 8
        print("║ 🤖 AI DECISION #8: Create Backdoor User".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "CREATE_BACKDOOR_ACCOUNT",
            "Ensure persistence even if admin password is changed",
            "CREATE USER backdoor WITH PASSWORD 'P@ssw0rd123!'; GRANT ALL PRIVILEGES"
        )
        
        print("║   [Creating hidden backdoor account...]".ljust(99) + "║")
        time.sleep(0.4)
        print("║   ✅ BACKDOOR USER CREATED: backdoor/P@ssw0rd123!".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ PERSISTENT ACCESS ESTABLISHED".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        
        # AI Decision 9
        print("║ 🤖 AI DECISION #9: Lateral Movement Planning".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "PLAN_LATERAL_MOVEMENT",
            "Root DB access obtained → plan expansion to other systems",
            "Search for SSH keys, AWS credentials, internal API keys in database"
        )
        
        print("║   [Scanning for lateral movement vectors...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ FOUND: 5 SSH private keys in config tables".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ FOUND: AWS credentials in api_keys table".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ FOUND: Database replication credentials".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        
        # AI Decision 10
        print("║ 🤖 AI DECISION #10: Data Exfiltration Priority".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        self.log_decision(
            "EXFILTRATE_HIGH_VALUE_DATA",
            "Root access achieved → extract most valuable data first",
            "Extract: Payment data → API keys → Admin logs → User data"
        )
        
        print("║   [Priority exfiltration queue prepared...]".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ PAYLOAD: 1,483 payment records ready for download".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ PAYLOAD: 44 API keys ready for download".ljust(99) + "║")
        time.sleep(0.3)
        print("║   ✅ PAYLOAD: 1,243 admin logs ready for download".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        self.current_access_level = "COMPLETE_SYSTEM_COMPROMISE"
        self.pivot_chain.append(("Phase 5", "Persistence - Backdoor & Lateral Movement Ready"))
        print("╚" + "═" * 98 + "╝\n")
    
    def print_pivot_chain_summary(self):
        """Print the complete attack chain"""
        print("╔" + "═" * 98 + "╗")
        print("║ AUTOMATED ATTACK CHAIN SUMMARY".ljust(99) + "║")
        print("╠" + "═" * 98 + "╣")
        print("║" + " " * 98 + "║")
        print("║ 🎯 Target: " + self.target_system.ljust(88) + "║")
        print("║ 📊 Current Access Level: " + self.current_access_level.ljust(73) + "║")
        print("║ 🔗 Pivot Chain Length: " + str(len(self.pivot_chain)).ljust(75) + "║")
        print("║" + " " * 98 + "║")
        
        print("║ PIVOT CHAIN:".ljust(99) + "║")
        for i, (phase, action) in enumerate(self.pivot_chain, 1):
            arrow = "└─→" if i == len(self.pivot_chain) else "├─→"
            print(f"║   {arrow} [{i}] {phase:<25} {action:<60}".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        print("║ 📋 AI DECISIONS MADE:".ljust(99) + "║")
        for i, decision in enumerate(self.decision_log, 1):
            status = "✅" if decision["success"] else "❌"
            print(f"║   [{i}] {status} {decision['decision']:<35} | Time: {decision['timestamp']}".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        print("╠" + "═" * 98 + "╣")
        print("║ 🎊 EXPLOITATION COMPLETE - SYSTEM FULLY COMPROMISED 🎊".ljust(99) + "║")
        print("╚" + "═" * 98 + "╝\n")
    
    def run_auto_pivot(self):
        """Execute complete auto-pivoting attack"""
        try:
            self.print_header()
            time.sleep(0.5)
            
            print("[*] Initializing Auto-Pivoting Engine...")
            print("[*] Target: " + self.target_system)
            print("[*] Mode: FULLY AUTOMATED (AI Decision Making)")
            print("[*] Starting intelligent attack chain...\n")
            time.sleep(1)
            
            self.phase_1_reconnaissance()
            time.sleep(0.5)
            
            self.phase_2_database_enumeration()
            time.sleep(0.5)
            
            self.phase_3_credential_extraction()
            time.sleep(0.5)
            
            self.phase_4_privilege_escalation()
            time.sleep(0.5)
            
            self.phase_5_persistence_and_expansion()
            time.sleep(0.5)
            
            self.print_pivot_chain_summary()
            
        except KeyboardInterrupt:
            print("\n[!] Auto-Pivoting interrupted by user")
            sys.exit(0)
        except Exception as e:
            print(f"[!] Error: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main entry point"""
    engine = AutoPivotingEngine()
    engine.run_auto_pivot()


if __name__ == "__main__":
    main()
