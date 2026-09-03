# Caesar Cipher Tool

**DecodeLabs Internship — Project 2 (Cryptographic Track)**

A Python command-line tool that encrypts and decrypts text using a Caesar cipher — a classic substitution cipher where every letter is shifted a fixed number of positions in the alphabet.

## What it does

1. Takes a line of text and a numeric shift key from the user
2. **Encrypts** the text by shifting every letter forward by the shift key
3. **Decrypts** the result by shifting backward by the same key, recovering the original text
4. Leaves spaces, numbers, and punctuation untouched — only letters are shifted

## The math

Each letter is converted to a number (its position in the alphabet, 0–25), shifted, then converted back:

```
Encrypt: E(x) = (x + n) % 26
Decrypt: D(x) = (x - n) % 26
```

Where `x` is the letter's position and `n` is the shift key. The `% 26` (modulo) makes the alphabet "wrap around" — so shifting `Z` forward by 3 correctly produces `C`, instead of an invalid value outside the alphabet.

This is a **symmetric cipher**: the same key both encrypts and decrypts, just applied in opposite directions.

## How to run it

```bash
python caesar_cipher.py
```

You'll be prompted for text and a shift key. The program prints the original, encrypted, and decrypted text so you can confirm the round-trip works. Type `quit` to exit.

### Example

```
Enter text: Hello World
Enter shift key (e.g. 3): 3

Original:   Hello World
Encrypted:  Khoor Zruog
Decrypted:  Hello World
```

## Design notes

- **`decrypt()` reuses `encrypt()`** with a negated shift, instead of duplicating the shifting logic — since Caesar cipher decryption is mathematically just encryption in reverse, this avoids repeating code and reduces the chance of bugs.
- **Non-letters pass through unchanged** — the `isupper()`/`islower()` checks ensure spaces, punctuation, and digits aren't corrupted by the shift, which a naive character-by-character shift (without these checks) would break.
- **Negative shifts work correctly** — Python's `%` operator handles negative numbers safely, so a shift of `-3` still wraps around the alphabet correctly instead of producing invalid characters.
- **Input validation on the shift key** — wrapping `int(input(...))` in a `try/except` prevents the program from crashing if the user types a non-numeric shift value, and instead prompts them to try again.

## Known limitation (and why it matters)

The Caesar cipher is a **lockbox, not a vault** — it's a good exercise in encryption logic, but it is not cryptographically secure:

- It only has 25 possible keys, so it can be brute-forced instantly by a computer
- It preserves the frequency distribution of letters, meaning frequency analysis (comparing how often each letter appears) can reveal the shift key even without brute-forcing

Real-world systems use algorithms like **AES-256**, which apply much larger keys and additional techniques (confusion and diffusion) to resist these attacks.

## Possible future improvements

- Implement a **Vigenère cipher** — uses a repeating keyword instead of a single number, closing the frequency-analysis weakness
- Add a brute-force "crack this" mode that tries all 25 shifts and shows the results, to demonstrate the vulnerability firsthand
- Support encrypting/decrypting entire text files, not just single lines of input

## Author

Osazuwa — DecodeLabs Cybersecurity Internship, Batch 2026
