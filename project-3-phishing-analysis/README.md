# Phishing Red-Flag Scanner

**DecodeLabs Internship — Project 3 (Detection Track)**

A Python command-line tool that scans email/message text for common phishing indicators and produces a Safe / Suspicious / Malicious verdict, along with a breakdown of exactly which red flags were detected.

## What it does

The scanner checks a message against three categories of common phishing red flags:

1. **Urgency/pressure language** — phrases designed to create false time pressure and short-circuit careful thinking (e.g. "act now", "account suspended", "24 hours")
2. **Requests for sensitive information** — phrases asking for passwords, bank details, OTPs, or other information legitimate organizations rarely request over email/message
3. **Suspicious link patterns** — common link-shortener domains and phrasing used to disguise malicious URLs (e.g. "bit.ly", "click here", "secure-login")

## How scoring works

Each matched keyword/phrase across all three categories counts as one flag.

| Total flags | Verdict |
|---|---|
| 0 | Safe |
| 1–2 | Suspicious |
| 3+ | Malicious |

Each verdict comes with a recommended action, following the **Pause → Verify → Report** framework:
- **Safe** — no action needed, but stay alert to anything unexpected
- **Suspicious** — warn the user, verify the sender through a separate channel before acting
- **Malicious** — do not click any links or reply; report to the security team and block the sender

## How to run it

```bash
python phishing_scanner.py
```

Paste in the text of a message, then type `END` on its own line to submit it for scanning. The tool will print a report showing the verdict and which specific red flags were found. Type `quit` to exit.

### Example

```
Enter message text (finish with a line containing only END):
URGENT: Your account will be suspended in 24 hours. Click here to verify your account and confirm your details immediately.
END

--- Phishing Scan Report ---
Verdict: Malicious
Total red flags found: 5

Urgency/pressure language detected: ['urgent', 'suspended', '24 hours', 'immediately']
Requests for sensitive info detected: ['verify your account', 'confirm your details']
Suspicious link patterns detected: ['click here']

Recommended action: Do not click any links or reply. Report to security team and block sender.
-----------------------------
```

## Design notes

- **Keyword lists organized by category** — this mirrors the standard red-flag taxonomy used in phishing awareness training (urgency, sensitive-info requests, suspicious links), making the tool's logic easy to explain and extend.
- **Multi-line input with an `END` marker** — real phishing emails are rarely a single line, so the scanner accepts a full pasted message body rather than just one line of input.
- **Simple additive scoring** — reuses the same pattern as the Project 1 password checker (count matches, classify by threshold), keeping the logic consistent and easy to reason about across projects.
- **Every verdict maps to a concrete recommended action** — this ties the tool directly to the Pause → Verify → Report framework, so it's not just a classifier but an actual decision-support tool.

## Written analysis

See `phishing_analysis.md` in this folder for the applied analysis of sample phishing messages, including a breakdown of red flags found in each and why they're unsafe.

## Known limitation

This is a keyword-based scanner, not a full email security tool — it doesn't inspect actual email headers, sender domains, or embedded links the way real anti-phishing systems do (SPF/DKIM/DMARC checks, domain reputation, etc.). It's a training exercise in pattern recognition and triage logic, not a production-grade filter.

## Possible future improvements

- Parse actual email headers (From/Return-Path) to detect sender-domain mismatches
- Check URLs against a domain reputation list instead of just keyword matching
- Expand the keyword lists based on real reported phishing samples

## Author

Osazuwa — DecodeLabs Cybersecurity Internship, Batch 2026
