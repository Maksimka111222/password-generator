import argparse

from src.generator import generate_password
from src.strength import check_strength


def main():
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument("-l", "--length", type=int, default=16)
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    args = parser.parse_args()

    password = generate_password(
        args.length,
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
    )
    print(f"Password: {password}")
    print(f"Strength: {check_strength(password)}")


if __name__ == "__main__":
    main()
