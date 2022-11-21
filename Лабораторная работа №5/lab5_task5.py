import random
def get_random_password(str) -> str:
    n = 8
    import string
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return str(random.sample(symbols, n))

print(get_random_password(str))
