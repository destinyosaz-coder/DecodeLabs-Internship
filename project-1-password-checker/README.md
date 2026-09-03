# Password Strength Checker

**DecodeLabs Internship — Project 1 (Defensive Track)**

A Python command-line tool that evaluates whether a password is **Weak**, **Medium**, or **Strong**, and explains exactly what's missing.

## What it does

The checker evaluates a password against five criteria:

1. **Length** — at least 8 characters
2. **Uppercase letter** — at least one `A-Z`
3. **Lowercase letter** — at least one `a-z`
4. **Digit** — at least one `0-9`
5. **Symbol** — at least one special character (e.g. `! @ # $ %`)

It also checks the password against a list of commonly leaked/weak passwords (e.g. `123456`, `password`, `qwerty`) and immediately flags these as **Weak**, regardless of length or character variety — because attackers try these first, no matter how "complex" they look.

## How scoring works

Each of the five criteria above contributes 1 point if satisfied (max score: 5).

| Score | Strength |
|-------|----------|
| 0–2   | Weak     |
| 3–4   | Medium   |
| 5     | Strong   |

A password that matches the common-password list is scored **Weak** automatically, before the point system is even applied — the goal is defensive logic, not just a numeric score.

## How to run it

```bash
python password_checker.py
```

You'll be prompted to enter a password. The program will print the strength result and specific suggestions for improvement. Type `quit` to exit.

### Example

```
Enter your password: password123
Password Strength: Medium
- Add at least one uppercase letter
- Add at least one symbol (e.g. ! @ # $)
```

## Design notes

- **`COMMON_PASSWORDS` is a `set`, not a list** — membership checks (`in`) on a set are O(1) on average, versus O(n) for a list. This matters as the common-password list grows.
- **Common-password and empty-input checks run before the scoring logic** — these are guard clauses that handle special cases explicitly and keep the main scoring logic simple and linear.
- **`any(condition for char in password)`** is used instead of manual `for` loops with a flag variable — it's both more readable and short-circuits (stops as soon as it finds a match), which is more efficient than scanning the whole string every time.
- **Logic is separated from I/O** — `check_password_strength()` contains the pure logic and returns a value, while `main()` handles user interaction. This makes the checking logic reusable and easier to test independently of the command-line interface.

## Possible future improvements

- Load the common-password list from a larger breach database file instead of a hardcoded set
- Penalize repeated or sequential characters (e.g. `aaaa1111`, `abcd1234`)
- Add unit tests for `check_password_strength()`
- Use `hmac.compare_digest()` for constant-time comparisons if this is ever extended to check against stored hashes (prevents timing attacks)

## Author

Osazuwa — DecodeLabs Cybersecurity Internship, Batch 2026
