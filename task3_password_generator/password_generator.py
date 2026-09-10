"""
TASK 3 · Random Password Generator (Beginner Tier)
----------------------------------------------------
Command-line password generator based on user-defined criteria.

Checklist covered:
[x] Prompt user to specify desired password length (minimum 8 characters enforced)
[x] Prompt user to choose character types (uppercase, lowercase, numbers, symbols) —
    at least 2 types must be selected
[x] Generate and display a password matching all specified criteria
[x] Input validation: reject invalid lengths or no character types selected
[x] Option to generate another password without restarting the program
"""

import random
import string

MIN_LENGTH = 8


def get_length() -> int:
    while True:
        raw = input(f"Enter desired password length (minimum {MIN_LENGTH}): ").strip()
        if not raw.isdigit():
            print(f"  ⚠  '{raw}' is not a valid whole number. Try again.")
            continue

        length = int(raw)
        if length < MIN_LENGTH:
            print(f"  ⚠  Length must be at least {MIN_LENGTH} characters. Try again.")
            continue

        return length


def get_character_types() -> dict:
    print("\nChoose character types to include (y/n for each).")
    print("You must select at least 2 types.\n")

    while True:
        options = {
            "uppercase": input("  Include UPPERCASE letters? (y/n): ").strip().lower() == "y",
            "lowercase": input("  Include lowercase letters? (y/n): ").strip().lower() == "y",
            "numbers":   input("  Include numbers?          (y/n): ").strip().lower() == "y",
            "symbols":   input("  Include symbols?          (y/n): ").strip().lower() == "y",
        }

        selected_count = sum(options.values())
        if selected_count < 2:
            print(f"  ⚠  You selected only {selected_count} type(s). Please select at least 2.\n")
            continue

        return options


def build_character_pool(options: dict) -> str:
    pool = ""
    if options["uppercase"]:
        pool += string.ascii_uppercase
    if options["lowercase"]:
        pool += string.ascii_lowercase
    if options["numbers"]:
        pool += string.digits
    if options["symbols"]:
        pool += string.punctuation
    return pool


def generate_password(length: int, options: dict) -> str:
    pool = build_character_pool(options)
    return "".join(random.choice(pool) for _ in range(length))


def main():
    print("=" * 45)
    print("      PYTHON RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        length = get_length()
        options = get_character_types()

        password = generate_password(length, options)

        print("\n--- Generated Password ---")
        print(f"  {password}")
        print("-" * 30)

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay secure.")
            break


if __name__ == "__main__":
    main()
