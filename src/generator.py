import secrets
import string


def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password with at least one char from each selected class."""
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+")
    if length < len(pools):
        raise ValueError("Length is too short for selected options")
    chars = "".join(pools)
    result = [secrets.choice(p) for p in pools]
    result += [secrets.choice(chars) for _ in range(length - len(result))]
    secrets.SystemRandom().shuffle(result)
    return "".join(result)