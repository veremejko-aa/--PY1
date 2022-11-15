def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    import random
    symbols = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789"
    return str(random.sample(symbols, 8))

print(get_random_password())
