'''
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
Задание
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt'''

import re

text = []
line_count = 0
file_name = 'referat.txt'

with open(file_name, 'r', encoding = 'utf-8') as f:
    for line in f:
        text.append(line)
        if line not in ['\n','','\t']:
            line_count += 1

print(f'1. Число строк в тексте файла {file_name}: {line_count}')

word_count = 0

for lines in text:
    word_count += len(re.split(r'\s', line ))

print(f'2. Число слов в тексте файла {file_name}: {word_count}')

with open('referat.txt', 'r', encoding='utf-8') as y:
    word_file = y.read()

print(f'3. Длинна файла {file_name}, считанного в переменную: {len(word_file)}')

word_file = word_file.replace('.', '!')

with open('refetat2.txt', 'w', encoding = 'utf-8') as new_file:
    new_file.write(word_file)
