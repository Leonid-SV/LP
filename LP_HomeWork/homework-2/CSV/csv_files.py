'''Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
Запишите содержимое списка словарей в файл в формате csv'''


import csv

users =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open('users.csv', 'w', encoding = 'utf-8', newline = '') as f:
    forms = ['name', 'age', 'job']

    writer = csv.DictWriter(f, forms, delimiter = ';')
    writer.writeheader()
    writer.writerows(users)