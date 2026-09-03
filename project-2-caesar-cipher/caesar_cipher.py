"""
Caesar Cipher - Encryption & Decryption
DecodeLabs Internship - Project 2
"""


def encrypt(text, shift):
    """Shift each letter forward by `shift` positions. Non-letters are unchanged."""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Leave spaces, numbers, and punctuation untouched
            result += char
    return result


def decrypt(text, shift):
    """Reverse the encryption by shifting backward — same logic, negative shift."""
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    print("Type 'quit' to exit.\n")

    while True:
        text = input("Enter text: ")
        if text.lower() == "quit":
            print("Goodbye!")
            break

        try:
            shift = int(input("Enter shift key (e.g. 3): "))
        except ValueError:
            print("Shift key must be a whole number. Try again.\n")
            continue

        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)

        print(f"\nOriginal:   {text}")
        print(f"Encrypted:  {encrypted}")
        print(f"Decrypted:  {decrypted}\n")


if __name__ == "__main__":
    main()