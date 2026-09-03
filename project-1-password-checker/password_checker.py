"""
Password Strength Checker
DecodeLabs Internship - Project 1

Evaluates a password's strength based on length, character variety,
and whether it matches a known list of commonly leaked/weak passwords.
"""

# A small sample of frequently leaked/common passwords.
# In production this would come from a much larger breach database.
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "qwerty", "abc123",
    "111111", "123123", "letmein", "welcome", "admin",
    "iloveyou", "password1", "12345678"
}


def check_password_strength(password):
    """
    Evaluate a password and return its strength as a string:
    'Weak', 'Medium', or 'Strong'.

    Also prints specific feedback explaining what's missing.
    """
    # Guard clause: handle empty or whitespace-only input first
    if not password.strip():
        print("\nPassword Strength: Weak")
        print("- Password cannot be empty")
        return "Weak"

    # Immediate fail for known common/leaked passwords, regardless of
    # how "complex" they look on paper — real attackers try these first.
    if password.lower() in COMMON_PASSWORDS:
        print("\nPassword Strength: Weak")
        print("- This password appears in common breach lists — choose something more unique")
        return "Weak"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)
    has_length = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_symbol, has_length])

    if score <= 2:
        strength = "Weak"
    elif score in (3, 4):
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")
    if not has_length:
        print("- Password should be at least 8 characters long")
    if not has_upper:
        print("- Add at least one uppercase letter")
    if not has_lower:
        print("- Add at least one lowercase letter")
    if not has_digit:
        print("- Add at least one number")
    if not has_symbol:
        print("- Add at least one symbol (e.g. ! @ # $)")

    return strength


def main():
    """Run the checker in a loop until the user chooses to quit."""
    print("=== Password Strength Checker ===")
    print("Type 'quit' at any time to exit.\n")

    while True:
        password = input("Enter your password: ")
        if password.lower() == "quit":
            print("Goodbye!")
            break
        check_password_strength(password)
        print()  # blank line for readability between attempts


if __name__ == "__main__":
    main()