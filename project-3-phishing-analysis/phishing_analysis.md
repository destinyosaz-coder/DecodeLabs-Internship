# Phishing Awareness Analysis

**DecodeLabs Internship — Project 3 (Detection Track)**

This document applies the red-flag framework from the training material to three sample messages, identifies the specific indicators present in each, and explains why each message is (or isn't) safe. Each sample was also run through `phishing_scanner.py` to confirm the automated verdict matches the manual analysis.

---

## Sample 1: Fake Account Suspension Notice

**Message text:**
> Subject: FW: Urgent Your Account Security Alert
> From: Microsoft Support <support@logins-updates.com>
>
> URGENT: Your account will be suspended in 24 hours due to unusual activity. Click here to verify your account and confirm your details immediately to avoid permanent lockout.

**Scanner result:** Malicious (5 flags)
- Urgency/pressure language: `urgent`, `suspended`, `24 hours`, `immediately`
- Requests for sensitive info: `verify your account`, `confirm your details`
- Suspicious link pattern: `click here`

**Manual red flags identified:**
1. **Sender-domain mismatch** — the display name says "Microsoft Support," but the actual domain (`logins-updates.com`) has no connection to Microsoft. This is the Red Flag 1 pattern from the training material: display name spoofing.
2. **Manufactured urgency** — "24 hours," "immediately," and "permanent lockout" are designed to trigger a fight-or-flight response so the reader acts before thinking.
3. **Generic vague threat** — the message doesn't reference any specific account, order, or activity, which is typical of mass-phishing (low personalization, high volume).
4. **"Click here" instead of a named destination** — legitimate account alerts typically link to a specific, named page; vague link text is used to hide the actual destination.

**Why it's unsafe:** This message combines authority impersonation (posing as Microsoft), urgency, and a credential-harvesting link — the three classic ingredients of a mass-phishing credential theft attempt. Clicking the link would likely lead to a fake login page designed to steal the victim's actual Microsoft credentials.

**Recommended action (Pause → Verify → Report):**
- **Pause:** Don't click the link. Recognize the urgency as a manipulation tactic.
- **Verify:** Go directly to a known-good URL (typed manually, not clicked) or the official Microsoft app to check account status — never through a link in the email itself.
- **Report:** Report the email to IT/security and delete it.

---

## Sample 2: Business Email Compromise (Fake Wire Transfer Request)

**Message text:**
> From: CEO Name <ceo.urgent@executive-update.com>
> Subject: IMMEDIATE ACTION REQUIRED: Transfer Authorization
>
> URGENT: Process the attached wire transfer instruction immediately. This is critical and must remain strictly confidential. Do not discuss this with anyone. Bypass standard procedure. Thank you.

**Scanner result:** Suspicious (2 flags — `urgent`, `immediately`; this scanner's keyword list doesn't include phrases like "confidential" or "bypass," which is a known limitation noted in the README)

**Manual red flags identified:**
1. **Authority impersonation** — posing as the CEO to demand unquestioned compliance, a classic "whaling" tactic targeting finance staff.
2. **Explicit secrecy demand** — "do not discuss with anyone" is a major red flag; legitimate financial processes do not require secrecy from colleagues.
3. **Explicit bypass request** — "bypass standard procedure" directly asks the recipient to skip normal verification steps, which no legitimate instruction should ever require.
4. **Domain mismatch** — the sender's domain (`executive-update.com`) doesn't match the company's actual domain, consistent with true domain spoofing or a lookalike domain.

**Why it's unsafe:** This is a textbook Business Email Compromise (BEC) attempt. The combination of urgency, secrecy, and a bypass request is designed to isolate the target from anyone who might catch the fraud — this exact pattern has been used in real attacks resulting in multi-million-dollar losses (e.g., the Quanta Computer domain-spoofing case referenced in the training material).

**Note on scanner limitation:** This sample shows why keyword scanning alone isn't sufficient — the scanner only caught 2 of the 4 real red flags because "confidential" and "bypass standard procedure" weren't in its keyword list. This is documented as a known limitation in the project README, and highlights why human judgment and the Pause-Verify-Report habit remain essential even with automated tools.

**Recommended action (Pause → Verify → Report):**
- **Pause:** Secrecy + urgency + a request to skip procedure is never legitimate — stop immediately.
- **Verify:** Call the CEO directly using a known phone number (not one provided in the email) to confirm the request out-of-band.
- **Report:** Escalate to finance leadership and security immediately, even if the transfer hasn't been made yet.

---

## Sample 3: Routine Internal Message (Safe Control Sample)

**Message text:**
> From: Sarah Lee <sarah.lee@company.com>
> Subject: Q3 Project Status Update - Non-Urgent
>
> Hi Team, please review the attached project status for Q3 at your earliest convenience. No immediate action is required. Thanks, Sarah.

**Scanner result:** Safe (0 flags)

**Manual analysis:**
- Sender domain matches the company's actual domain
- No urgency language — explicitly states "no immediate action is required"
- No request for sensitive information
- No suspicious links, only a named attachment
- Tone and content are consistent with routine internal communication

**Why it's safe:** This message has none of the psychological manipulation tactics (urgency, secrecy, authority pressure) or technical red flags (domain mismatch, suspicious links) present in the other two samples. It's included as a control sample to confirm the scanner doesn't flag legitimate messages as false positives.

**Recommended action:** No action needed beyond normal review. This illustrates that not every message needs the Pause-Verify-Report response — only those exhibiting genuine red flags.

---

## Summary Table

| Sample | Verdict | Key red flags | Recommended action |
|---|---|---|---|
| 1. Fake account suspension | Malicious | Domain mismatch, urgency, credential-harvesting link | Block & Escalate |
| 2. Fake CEO wire transfer | Malicious (manual) / Suspicious (scanner) | Authority impersonation, secrecy demand, bypass request | Block & Escalate |
| 3. Routine internal update | Safe | None | Close |

## Key takeaway

Automated keyword scanning (like `phishing_scanner.py`) is a useful first line of triage, but Sample 2 shows its limits — a scanner is only as good as its keyword list, and sophisticated attacks (like BEC) often use phrasing that doesn't trip simple pattern matching. The Pause → Verify → Report habit, applied by a trained human, remains the most reliable defense — this is exactly why the training material frames people as "the human firewall" rather than relying on technical filters alone.

## Author

Osazuwa — DecodeLabs Cybersecurity Internship, Batch 2026
