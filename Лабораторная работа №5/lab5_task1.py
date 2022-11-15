# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_of_dictionaries = [] #создаем пустой список

for x in range(16):

    dict = {"bin": bin(x), "dec": x, "hex": hex(x), "oct": oct(x)}
    list_of_dictionaries = [dict for x in range(16)]

pprint(list_of_dictionaries)
