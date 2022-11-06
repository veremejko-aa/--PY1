def get_count_char(str_):
    list_words = str_.split()  # получили список отдельных слов
    list_words.sort # сортируем список в алфовитном порядке
    new_str = "".join(list_words) # склеиваем в строку
    new_lower_str = new_str.lower() # приводим строку к нижнему регистру

    letters_dict = {}
    DEFAULT_COUNT = 0

    for letter in new_lower_str:
        if letter.isalpha():
            letters_dict[letter] = letters_dict.get(letter, DEFAULT_COUNT) + 1

    def get_percentage_char(letters_dict):

        percentage = 0  # процент

        for letter in letters_dict:
            if letter.isalpha():
                letters_dict[letter] = (letters_dict.get(letter, percentage) + 1) / len(str_) * 100

    return letters_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

count_dict = get_count_char(main_str)

def get_percentage_char(letters_dict, str_):

    percentage = 0  # процент

    for letter in letters_dict:
        if letter.isalpha():
            letters_dict[letter] = (letters_dict.get(letter, percentage) + 1) / len(str_) * 100

    return letters_dict

print(get_percentage_char(count_dict, main_str))
