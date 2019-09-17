# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(f'последняя букву в слове: {word[-1]}')

# Вывести количество букв "а" в слове
word = 'Архангельск'
print('количество букв "а" в слове {}: {}'.format(word, word.upper().count('А')))


# Вывести количество гласных букв в слове
word = 'Архангельск'
pr = ('а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я')

pr_sum = 0

for s in pr:
    pr_sum += word.lower().count(s)

print('количество гласных букв в слове {}: {}'.format(word, pr_sum))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print('количество слов в предложении: {}'.format(len(sentence.split())))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
print('первая буква каждого слова на отдельной строке:')
for w in sentence.split():
    print(w[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

from numpy import average
av = average(list(map(len, sentence.split())))
print(f'усреднённую длину слова: {av}')