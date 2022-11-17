from random import randint

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    list_unique_numbers = []
    for i in range(15):
        list_unique_numbers.append(randint(-10, 10))

    return list_unique_numbers



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
