"""
Phishing Red-Flag Scanner
DecodeLabs Internship - Project 3

Scans a block of email/message text for common phishing indicators
and produces a simple Safe / Suspicious / Malicious verdict.
"""

# Words/phrases that create false urgency or pressure — a classic
# cognitive trigger attackers use to make people act before thinking.
URGENCY_WORDS = [
    "urgent", "immediately", "act now", "verify your account",
    "suspended", "locked", "expire", "24 hours", "final notice",
    "act fast", "limited time"
]

# Phrases that ask for sensitive info directly over email/message —
# legitimate organizations rarely ask for these this way.
SENSITIVE_REQUESTS = [
    "password", "social security", "credit card", "bank account",
    "verify your identity", "confirm your details", "pin number",
    "wire transfer", "otp", "one-time code"
]

# Common lookalike / suspicious link patterns
SUSPICIOUS_LINK_HINTS = [
    "bit.ly", "tinyurl", "click here", "confirm-account",
    "secure-login", "login-update", ".xyz", ".top", ".info"
]


def scan_message(text):
    """
    Scan message text and return a dict with:
    - found flags (what was detected, grouped by category)
    - a verdict: Safe, Suspicious, or Malicious
    """
    text_lower = text.lower()

    urgency_hits = [w for w in URGENCY_WORDS if w in text_lower]
    sensitive_hits = [w for w in SENSITIVE_REQUESTS if w in text_lower]
    link_hits = [w for w in SUSPICIOUS_LINK_HINTS if w in text_lower]

    total_flags = len(urgency_hits) + len(sensitive_hits) + len(link_hits)

    if total_flags == 0:
        verdict = "Safe"
    elif total_flags <= 2:
        verdict = "Suspicious"
    else:
        verdict = "Malicious"

    return {
        "urgency_flags": urgency_hits,
        "sensitive_info_flags": sensitive_hits,
        "suspicious_link_flags": link_hits,
        "total_flags": total_flags,
        "verdict": verdict
    }


def print_report(text):
    """Run the scan and print a readable report."""
    result = scan_message(text)

    print("\n--- Phishing Scan Report ---")
    print(f"Verdict: {result['verdict']}")
    print(f"Total red flags found: {result['total_flags']}")

    if result["urgency_flags"]:
        print(f"\nUrgency/pressure language detected: {result['urgency_flags']}")
    if result["sensitive_info_flags"]:
        print(f"Requests for sensitive info detected: {result['sensitive_info_flags']}")
    if result["suspicious_link_flags"]:
        print(f"Suspicious link patterns detected: {result['suspicious_link_flags']}")

    if result["verdict"] == "Safe":
        print("\nNo obvious red flags found. Still apply the Pause-Verify-Report habit for anything unexpected.")
    elif result["verdict"] == "Suspicious":
        print("\nRecommended action: Warn user, verify sender through a separate channel before acting.")
    else:
        print("\nRecommended action: Do not click any links or reply. Report to security team and block sender.")
    print("-----------------------------\n")


def main():
    print("=== Phishing Red-Flag Scanner ===")
    print("Paste an email/message below. Type 'END' on its own line when done, or 'quit' to exit.\n")

    while True:
        print("Enter message text (finish with a line containing only END):")
        lines = []
        while True:
            line = input()
            if line.strip().lower() == "quit":
                print("Goodbye!")
                return
            if line.strip().upper() == "END":
                break
            lines.append(line)

        message = "\n".join(lines)
        if message.strip():
            print_report(message)


if __name__ == "__main__":
    main()