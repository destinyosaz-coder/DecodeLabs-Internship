# Personal System Security Audit

**DecodeLabs Internship — Project 4 (Audited Systems / Blue Team Defense)**

An automated PowerShell audit tool that checks a Windows machine against a 4-step security checklist — identity/access hygiene, patch management, admin account review, and network/disk hardening — then reports findings in a color-coded PASS/FAIL format with severity ratings.

## What it does

`security_audit.ps1` runs five checks across four categories:

1. **Identity & Access** — verifies the built-in Guest account is disabled
2. **Patch Management** — checks how recently Windows was last updated
3. **Human Perimeter** — lists all accounts with local administrator rights, for a least-privilege review
4. **Network & Endpoint Hygiene** — verifies the Windows Firewall is active on all three profiles (Domain, Private, Public), and confirms the primary drive is protected with BitLocker disk encryption

Each check is reported as PASS, FAIL, or INFO, with a CVSS-aligned severity rating (Critical/High/Medium) attached to any failure, and a summary count at the end.

## How to run it

Open PowerShell **as Administrator** (several checks require elevated rights to return accurate results), navigate to this folder, and run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\security_audit.ps1
```

The `Set-ExecutionPolicy` line is a one-time, session-only permission to run local scripts — it doesn't change your system's permanent security settings.

### Example output

```
[Endpoint] Disk Encryption (BitLocker)
  Status: FAIL
  Detail: C: drive protection is OFF
  Severity: Critical
```

## The audit report

See `vulnerability_report.md` in this folder for the full 1-page findings report, including the specific flaw identified on my own machine (disk encryption disabled), the remediation steps taken, and before/after proof that the fix worked.

## Design notes

- **Automated over manual** — rather than running each checklist command by hand and copy-pasting results, this script runs the entire audit in one pass and produces a consistent, repeatable report — the kind of tooling a real security team would want for recurring audits, not just a one-time check.
- **Severity-rated findings** — failures are tagged with a CVSS-aligned severity (Critical/High/Medium), matching how real vulnerability management prioritizes remediation effort by risk, not just by a flat pass/fail list.
- **`Report-Finding` as a reusable function** — centralizes the pass/fail/color-coding logic instead of repeating print statements for every check, making the script easy to extend with additional checks later.
- **BitLocker check wrapped in try/catch** — `Get-BitLockerVolume` throws an error rather than returning a clean false result if BitLocker isn't available (e.g. on Windows Home editions) or if the script isn't run as Administrator; the try/catch ensures the script still produces a clear, readable finding instead of crashing.

## Known limitation

This audit checks only a fixed set of common misconfigurations and is scoped to Windows via PowerShell cmdlets. It doesn't cover every item in the training material's checklist (e.g., MFA/authenticator type, browser-specific patch levels, or physical security like screen-lock timeout) — those were reviewed manually rather than scripted, per the audit report.

## Possible future improvements

- Add a macOS equivalent using the Terminal command matrix from the training material (`socketfilterfw`, `fdesetup`, `dscl`)
- Add a screen-lock timeout check and browser version check
- Export findings to a CSV or JSON file automatically instead of just console output

## Author

Osazuwa — DecodeLabs Cybersecurity Internship, Batch 2026
