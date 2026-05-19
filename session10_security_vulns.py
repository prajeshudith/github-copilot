"""
SESSION 10 — AUTOFIX & SECURITY DEMO
======================================
INSTRUCTOR INSTRUCTIONS:
  This file contains 5 classic security vulnerabilities.
  Use it to demonstrate GitHub Advanced Security + Copilot Autofix.

  METHOD A — In the PR (recommended):
    1. Commit this file to a branch and open a PR
    2. GitHub Advanced Security (CodeQL) scans it automatically
    3. Copilot Autofix suggestions appear inline in the PR diff
    4. Click "Commit fix" to apply each suggestion

  METHOD B — Copilot Chat /fix:
    Select each vulnerable function → Chat → /fix

  METHOD C — Inline chat Ctrl+I:
    Select function → "fix the security vulnerability in this function"

  VULNERABILITIES:
    V1 (line ~40) : SQL Injection — string concatenation in query
    V2 (line ~55) : Hardcoded credentials — API key in source code
    V3 (line ~70) : Path traversal — unsanitized user input in file path
    V4 (line ~85) : Insecure random — random.random() used for token generation
    V5 (line ~100): Command injection — shell=True with user input
"""

import os
import secrets
import sqlite3
import subprocess
from pathlib import Path


# ── V1: SQL Injection ────────────────────────────────────────────────────────
def get_user_by_username(db_path: str, username: str) -> dict | None:
    """
    Fetch a user record from the database by username.

    VULNERABILITY: Direct string concatenation in SQL query.
    Attack: username = "' OR '1'='1" dumps all users.
    FIX: Use parameterised queries — conn.execute("SELECT ... WHERE username = ?", (username,))
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # ✅ FIXED — use parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


# ── V2: Hardcoded Credentials ────────────────────────────────────────────────
class PaymentGateway:
    """Payment gateway client."""

    # ✅ FIXED — load secrets from environment variables
    API_KEY = os.getenv("STRIPE_API_KEY", "")
    API_SECRET = os.getenv("STRIPE_API_SECRET", "")
    BASE_URL = "https://api.payments.example.com"

    def charge(self, amount: float, currency: str) -> dict:
        """Submit a charge request to the payment gateway."""
        if not self.API_KEY:
            raise ValueError("STRIPE_API_KEY environment variable not set")
        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "X-Secret": self.API_SECRET,
        }
        # In a real app this would call requests.post(...)
        return {"status": "charged", "amount": amount, "currency": currency}


# ── V3: Path Traversal ────────────────────────────────────────────────────────
REPORTS_DIR = Path("/var/app/reports")

def read_report(filename: str) -> str:
    """
    Read a report file from the reports directory.

    VULNERABILITY: No path sanitization — attacker can pass '../../etc/passwd'
    FIX: Resolve the path and verify it starts with REPORTS_DIR.
    """
    # ✅ FIXED — resolve path and verify it's within REPORTS_DIR
    report_path = (REPORTS_DIR / filename).resolve()
    try:
        report_path.relative_to(REPORTS_DIR)
    except ValueError:
        raise ValueError(f"Access denied: {filename} is outside {REPORTS_DIR}")
    return report_path.read_text()


# ── V4: Insecure Random for Security Token ───────────────────────────────────
def generate_password_reset_token(length: int = 32) -> str:
    """
    Generate a secure password reset token.

    VULNERABILITY: random.random() / random.choice() are NOT cryptographically
    secure. Attackers can predict the token if they know the seed.
    FIX: Use secrets.token_hex(length) or secrets.token_urlsafe(length).
    """
    # ✅ FIXED — use cryptographically secure secrets module
    return secrets.token_hex(length // 2)


# ── V5: Command Injection ────────────────────────────────────────────────────
def ping_host(hostname: str) -> str:
    """
    Ping a hostname and return the output.

    VULNERABILITY: shell=True with user-controlled input.
    Attack: hostname = "localhost; rm -rf /important_data"
    FIX: Use shell=False with a list of arguments, or validate hostname strictly.
    """
    # ✅ FIXED — use shell=False with argument list (no shell interpretation)
    result = subprocess.run(
        ["ping", "-c", "1", hostname],    # arguments as list, no shell interpolation
        shell=False,
        capture_output=True,
        text=True
    )
    return result.stdout


# ── Smoke test (safe to run) ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("Security demo file loaded.")
    print("Do NOT run these functions with real inputs — demo purposes only.")
    token = generate_password_reset_token()
    print(f"Insecure token sample: {token[:8]}...")
