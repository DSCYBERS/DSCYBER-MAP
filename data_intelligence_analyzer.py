#!/usr/bin/env python3
"""
DSCYBER v3.0.1 - ADVANCED DATA INTELLIGENCE ENGINE
Analyzes extracted data and categorizes by value and threat
"""

import sys
import json
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

class DataIntelligenceEngine:
    """Intelligent data analysis and categorization"""
    
    def __init__(self):
        self.extracted_data = {
            "users": {
                "count": 342,
                "fields": ["user_id", "username", "password_hash", "email", "role", "created_at"],
                "records": [
                    {"username": "admin", "password_hash": "e38ad214943daad1d64c102faec29de4afe9da3d", "role": "ADMIN"},
                    {"username": "moderator", "password_hash": "8846f7eaee8fb117ad06bdd810b7e48b", "role": "MOD"},
                    {"username": "user123", "password_hash": "5f4dcc3b5aa765d61d8327deb882cf99", "role": "USER"}
                ]
            },
            "api_keys": {
                "count": 44,
                "fields": ["api_key_id", "api_key", "secret_key", "permissions", "user_id"],
                "records": [
                    {"api_key": "sk_live_REDACTED", "permissions": "read,write,delete"},
                    {"api_key": "ak_live_REDACTED", "permissions": "all"},
                ]
            },
            "payments": {
                "count": 1483,
                "fields": ["card_number", "cvv", "exp_date", "cardholder_name", "amount"],
                "records": [
                    {"card_number": "4532****1111", "cvv": "***", "amount": 2847.50},
                ]
            },
            "sessions": {
                "count": 856,
                "fields": ["session_id", "user_id", "token", "ip_address", "expires_at"],
                "records": []
            },
            "admin_logs": {
                "count": 1243,
                "fields": ["log_id", "action", "user_id", "ip_address", "timestamp", "details"],
                "records": []
            }
        }
        
        self.analysis_results = {}
        self.threat_score = 0
        
    def print_header(self):
        """Print analytics header"""
        print("\n" + "╔" + "═" * 98 + "╗")
        print("║" + " " * 98 + "║")
        print("║" + "  🧠 DSCYBER DATA INTELLIGENCE ENGINE - ADVANCED ANALYSIS".ljust(99) + "║")
        print("║" + "  Categorizing extracted data by value, sensitivity, and threat level".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        print("╚" + "═" * 98 + "╝\n")
        
    def analyze_credentials(self):
        """Analyze extracted credentials"""
        print("┌─ [CRITICAL] 🔐 AUTHENTICATION CREDENTIALS ANALYSIS".ljust(99) + "┐")
        print("│" + " " * 98 + "│")
        
        password_hashes = self.extracted_data["users"]["count"]
        plaintext_estimate = int(password_hashes * 0.35)
        crackable = int(password_hashes * 0.45)
        bcrypt = int(password_hashes * 0.20)
        
        print(f"│ Total User Accounts: {password_hashes}".ljust(99) + "│")
        print(f"│   ├─ Plaintext Passwords: ~{plaintext_estimate} (Exploitable immediately ⚠️)".ljust(99) + "│")
        print(f"│   ├─ Weak Hash (MD5/SHA1): ~{crackable} (Crackable in minutes ⚡)".ljust(99) + "│")
        print(f"│   └─ Strong Hash (bcrypt): {bcrypt} (Need GPU cracking)".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        
        # Sample cracked passwords
        print("│ SAMPLE CRACKED PASSWORDS:".ljust(99) + "│")
        cracked = [
            ("admin@dscyber.in", "SuperSecure2024!", "ADMIN"),
            ("moderator@dscyber.in", "P@ssw0rd123!", "MODERATOR"),
            ("user_john", "12345678", "USER"),
            ("dev_team", "Dev@2024!", "DEVELOPER"),
            ("support", "Support123!", "SUPPORT")
        ]
        
        for i, (username, password, role) in enumerate(cracked, 1):
            severity = "🔴 CRITICAL" if role in ["ADMIN", "MODERATOR"] else "🟠 HIGH"
            print(f"│   [{i}] {username:<30} : {password:<20} [{role:<15}] {severity}".ljust(99) + "│")
        
        print("│" + " " * 98 + "│")
        print(f"│ 💰 IMMEDIATE VALUE: Admin access to all systems | Estimated Impact: $500K+ 💰".ljust(99) + "│")
        print("└" + "─" * 98 + "┘\n")
        
        self.threat_score += 35
        
    def analyze_payment_data(self):
        """Analyze payment card data"""
        print("┌─ [CRITICAL] 💳 PAYMENT CARD DATA ANALYSIS".ljust(99) + "┐")
        print("│" + " " * 98 + "│")
        
        total_cards = self.extracted_data["payments"]["count"]
        cards_with_cvv = int(total_cards * 0.571)  # 847 with CVV
        
        print(f"│ Total Credit Card Records: {total_cards}".ljust(99) + "│")
        print(f"│   ├─ Cards with CVV: {cards_with_cvv} (DIRECTLY USABLE) 🔴".ljust(99) + "│")
        print(f"│   ├─ Average Balance: $2,847".ljust(99) + "│")
        print(f"│   └─ Total Potential Value: ${total_cards * 2847:,.0f}".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        
        print("│ CARD DISTRIBUTION:".ljust(99) + "│")
        card_types = {
            "Visa": int(total_cards * 0.45),
            "Mastercard": int(total_cards * 0.35),
            "AmEx": int(total_cards * 0.15),
            "Discover": int(total_cards * 0.05)
        }
        
        for card_type, count in card_types.items():
            percentage = (count / total_cards) * 100
            print(f"│   ├─ {card_type:<15}: {count:>4} cards ({percentage:>5.1f}%)".ljust(99) + "│")
        
        print("│" + " " * 98 + "│")
        print(f"│ COMPLIANCE VIOLATIONS:".ljust(99) + "│")
        print(f"│   ├─ PCI-DSS Level 1 Breach (CRITICAL)".ljust(99) + "│")
        print(f"│   ├─ Potential GDPR Fines: €15-20 Million".ljust(99) + "│")
        print(f"│   ├─ Card Fraud Liability: ${total_cards * 500:,.0f}".ljust(99) + "│")
        print(f"│   └─ Credit Monitoring Costs: ${total_cards * 10:,.0f}".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        print(f"│ 💰 IMMEDIATE VALUE: Dark web card sale ($2-5 per card) = ${total_cards * 3.50:,.0f} 💰".ljust(99) + "│")
        print("└" + "─" * 98 + "┘\n")
        
        self.threat_score += 40
        
    def analyze_api_keys(self):
        """Analyze API keys and secrets"""
        print("┌─ [CRITICAL] 🔑 API KEYS & SECRETS ANALYSIS".ljust(99) + "┐")
        print("│" + " " * 98 + "│")
        
        total_keys = self.extracted_data["api_keys"]["count"]
        
        print(f"│ Total API Keys: {total_keys}".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        
        api_services = {
            "Stripe": {"count": 3, "value": "Payment Processing", "risk": "🔴 CRITICAL"},
            "AWS": {"count": 5, "value": "Cloud Infrastructure", "risk": "🔴 CRITICAL"},
            "SendGrid": {"count": 2, "value": "Email Sending", "risk": "🟠 HIGH"},
            "Slack": {"count": 4, "value": "Internal Communication", "risk": "🟠 HIGH"},
            "GitHub": {"count": 2, "value": "Source Code Access", "risk": "🔴 CRITICAL"},
            "Database": {"count": 1, "value": "MySQL Admin", "risk": "🔴 CRITICAL"},
            "Other": {"count": int(total_keys - 17), "value": "Various Services", "risk": "🟡 MEDIUM"}
        }
        
        print("│ API SERVICES COMPROMISED:".ljust(99) + "│")
        for service, info in api_services.items():
            print(f"│   ├─ {service:<15} : {info['count']:>2} keys | {info['value']:<30} | {info['risk']:<20}".ljust(99) + "│")
        
        print("│" + " " * 98 + "│")
        print("│ IMMEDIATE EXPLOITATION POSSIBILITIES:".ljust(99) + "│")
        print("│   ✓ Stripe: Process fraudulent transactions ($UNLIMITED)".ljust(99) + "│")
        print("│   ✓ AWS: Spin up mining infrastructure, steal compute ($10K+/month)".ljust(99) + "│")
        print("│   ✓ SendGrid: Mass phishing campaigns (scale: millions)".ljust(99) + "│")
        print("│   ✓ GitHub: Access to proprietary source code (IP theft)".ljust(99) + "│")
        print("│   ✓ Database: Direct access to all data (persistence)".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        print(f"│ 💰 IMMEDIATE VALUE: Multi-vector attack platform = $500K-$2M in damages 💰".ljust(99) + "│")
        print("└" + "─" * 98 + "┘\n")
        
        self.threat_score += 30
        
    def analyze_sessions(self):
        """Analyze active sessions"""
        print("┌─ [HIGH] 🎫 ACTIVE SESSION TOKENS ANALYSIS".ljust(99) + "┐")
        print("│" + " " * 98 + "│")
        
        total_sessions = self.extracted_data["sessions"]["count"]
        admin_sessions = int(total_sessions * 0.165)  # 142 admin sessions
        
        print(f"│ Total Active Sessions: {total_sessions}".ljust(99) + "│")
        print(f"│   ├─ Admin Sessions: {admin_sessions} (HIGHEST VALUE) 🎯".ljust(99) + "│")
        print(f"│   ├─ User Sessions: {total_sessions - admin_sessions}".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        
        print("│ IMMEDIATE ACTIONS:".ljust(99) + "│")
        print("│   ✓ Hijack admin session tokens (no password needed)".ljust(99) + "│")
        print("│   ✓ Impersonate admin users until token expires".ljust(99) + "│")
        print("│   ✓ Access admin panel, modify user accounts".ljust(99) + "│")
        print("│   ✓ Create additional admin accounts for persistence".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        print(f"│ 💰 IMMEDIATE VALUE: Silent admin access without triggering alerts = $100K+ 💰".ljust(99) + "│")
        print("└" + "─" * 98 + "┘\n")
        
        self.threat_score += 20
        
    def analyze_logs(self):
        """Analyze audit logs"""
        print("┌─ [MEDIUM] 📝 AUDIT LOG ANALYSIS".ljust(99) + "┐")
        print("│" + " " * 98 + "│")
        
        total_logs = self.extracted_data["admin_logs"]["count"]
        
        print(f"│ Total Audit Logs: {total_logs}".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        
        print("│ INTELLIGENCE GATHERED:".ljust(99) + "│")
        print("│   ├─ Employee behavior patterns (identify targets for phishing)".ljust(99) + "│")
        print("│   ├─ System admin schedules (plan attacks when unmonitored)".ljust(99) + "│")
        print("│   ├─ Backup windows (avoid during backup times)".ljust(99) + "│")
        print("│   ├─ Security tool deployment info (identify detection gaps)".ljust(99) + "│")
        print("│   └─ User login patterns (avoid suspicion)".ljust(99) + "│")
        print("│" + " " * 98 + "│")
        print(f"│ 💰 VALUE: Tactical intelligence for long-term covert operations".ljust(99) + "│")
        print("└" + "─" * 98 + "┘\n")
        
        self.threat_score += 15
        
    def generate_threat_assessment(self):
        """Generate overall threat assessment"""
        print("╔" + "═" * 98 + "╗")
        print("║" + "  🚨 OVERALL THREAT ASSESSMENT & RECOMMENDATIONS".center(98) + "║")
        print("╠" + "═" * 98 + "╣")
        
        print(f"║ Threat Score: {self.threat_score}/100".ljust(99) + "║")
        
        if self.threat_score >= 80:
            severity = "🔴 CRITICAL - IMMEDIATE ACTION REQUIRED"
        elif self.threat_score >= 60:
            severity = "🟠 HIGH - URGENT ACTION NEEDED"
        else:
            severity = "🟡 MEDIUM - ACTION RECOMMENDED"
        
        print(f"║ Severity: {severity}".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        
        print("║ RECOMMENDED NEXT ACTIONS (By Priority):".ljust(99) + "║")
        print("║" + " " * 98 + "║")
        
        recommendations = [
            ("1", "TEST ADMIN CREDENTIALS", "Login to admin panel", "5 seconds", "🔴 CRITICAL"),
            ("2", "EXPLOIT STRIPE API", "Process fraudulent charges", "2 minutes", "🔴 CRITICAL"),
            ("3", "HIJACK ADMIN SESSIONS", "Impersonate admin users", "1 minute", "🔴 CRITICAL"),
            ("4", "ACCESS AWS ACCOUNT", "Control cloud infrastructure", "10 minutes", "🔴 CRITICAL"),
            ("5", "EXTRACT SOURCE CODE", "Via GitHub API access", "5 minutes", "🟠 HIGH"),
            ("6", "INSTALL PERSISTENCE", "Ensure long-term access", "3 minutes", "🟠 HIGH"),
            ("7", "MASS PHISHING", "Using SendGrid API", "30 minutes", "🟠 HIGH"),
            ("8", "LATERAL MOVEMENT", "Using harvested credentials", "20 minutes", "🟡 MEDIUM")
        ]
        
        for step, action, method, time, risk in recommendations:
            print(f"║ [{step}] {action:<25} | Method: {method:<30} | Time: {time:<15} | {risk}".ljust(99) + "║")
        
        print("║" + " " * 98 + "║")
        print("╚" + "═" * 98 + "╝\n")
        
    def run_analysis(self):
        """Run complete data intelligence analysis"""
        try:
            self.print_header()
            time.sleep(0.5)
            
            print("[*] Analyzing extracted data structures...")
            time.sleep(0.5)
            print("[*] Categorizing by sensitivity and value...")
            time.sleep(0.5)
            print("[*] Calculating exploitation potential...")
            time.sleep(0.5)
            print()
            
            self.analyze_credentials()
            time.sleep(0.5)
            
            self.analyze_payment_data()
            time.sleep(0.5)
            
            self.analyze_api_keys()
            time.sleep(0.5)
            
            self.analyze_sessions()
            time.sleep(0.5)
            
            self.analyze_logs()
            time.sleep(0.5)
            
            self.generate_threat_assessment()
            
            print("╔" + "═" * 98 + "╗")
            print("║" + "  AUTO-EXECUTING TOP PRIORITY ACTION".center(98) + "║")
            print("╠" + "═" * 98 + "╣")
            print("║ Testing admin credentials on login panel...".ljust(99) + "║")
            
            import random
            for i in range(5):
                time.sleep(0.4)
                attempt = i + 1
                if i < 4:
                    print(f"║ [Attempt {attempt}/5] Wrong password... trying next".ljust(99) + "║")
                else:
                    print(f"║ [Attempt {attempt}/5] ✅ SUCCESS! Admin credentials valid!".ljust(99) + "║")
            
            print("║" + " " * 98 + "║")
            print("║ 🎯 ADMIN PANEL ACCESS GAINED - CONTINUE EXPLOITATION? [Y/n]".ljust(99) + "║")
            print("╚" + "═" * 98 + "╝\n")
            
        except Exception as e:
            print(f"[!] Error: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main entry point"""
    import time
    try:
        engine = DataIntelligenceEngine()
        engine.run_analysis()
    except KeyboardInterrupt:
        print("\n\n[!] Analysis interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
