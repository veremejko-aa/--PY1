import random


def get_random_password(n=8) -> str:
    import string
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return str(random.sample(symbols, n))

print(get_random_password())
