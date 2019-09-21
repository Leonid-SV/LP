import csv
import os
import sys
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
print(dir_path)

from pprint import pprint

def get_key(dic, value):
    for key, v in dic.items():
        if v == value:
            return key


def read_cities_csv():
    # считывание из CSV-файла базу городов Росии
    with open('cities/ru_cities.csv', 'r', encoding=' Windows-1251') as c:
        fieldnames = ['city_name']
        reader = csv.DictReader(c, fieldnames)

        global cities_d

        cities_d = {}

        index = 0

        for row in reader:
            for key, value in row.items():
                cities_d[index] = value
                index += 1

read_cities_csv()
# pprint(cities_d)


def cities_by_last_simb(w: str, cit: dict):

# функция принемает символ или слово, получает последний символ слова и составляет словарь из тех имен городов, которые начинаются на этот символ

    cities_from_ls = {}
    index = 0

    back = 2 if w[-1] in ['й', 'ь', 'ъ', 'ё'] else 1

    for key, value in cit.items():
        if w[-back].upper() == value[0]:
            cities_from_ls[index] = value
            index += 1

    return cities_from_ls


def cities(w: str):
    global last_simb

    # Проверка ввода пользователя названия города с корректной буквы
    try:
        if last_simb == w[0].lower():
            pass
        else:
            return 'Не с той буквы название'
    except NameError:
        pass

    w = w.capitalize()

    print(f'step 1 in cities: {w}')

    if w in cities_d.values():

        cities_list_for_answer = cities_by_last_simb(w, cities_d)
        r_num = random.randint(1, len(cities_list_for_answer))
        answ = cities_list_for_answer[r_num]

        del cities_d[get_key(cities_d, w)]

        # получение последнего символа для проверке ввода пользователя
        last_simb = answ[-2 if answ[-1] in ['й', 'ь', 'ъ', 'ё'] else -1]

        return answ

    else:

        return 'Не знаю такого города или уже было'

