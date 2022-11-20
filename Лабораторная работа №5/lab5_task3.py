import random


def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    list_unique_numbers = []
    count_numbers = 0 #количество чисел в списке
    while count_numbers < 15:
        numbers = random.randint(-10, 10)

        if numbers not in list_unique_numbers:
            list_unique_numbers.append(numbers)
            count_numbers += 1


    return list_unique_numbers



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
