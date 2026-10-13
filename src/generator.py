import secrets
import string


def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password using the secrets module."""
    if length < 4:
        raise ValueError("Length must be at least 4")
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))