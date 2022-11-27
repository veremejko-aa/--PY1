import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', line_separator='\n') -> list[dict]:
    with open(filename) as f:
        list_of_dicts = []  # список словарей
        for index, line in enumerate(f):
            items = line.strip(line_separator).split(delimiter) #разграничиваем каждый элемент файла
            if index == 0: # первая строка - заголовки
                headers = items
                continue

            list_of_dicts.append({}) #новый словарь в нашем списке

            for i,_ in enumerate(headers):
                list_of_dicts[-1][headers[i]] = items[i] #добавляем словарь нужный элемент
    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

