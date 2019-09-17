from pprint import pprint

lst = [3, 5, 7, 9, 10.5]
pprint(lst)

lst.append('Python')

print(lst)
print(f'Длина списка: {len(lst)}')

print(f'Первый элмент списка {lst[0]}')
print(f'Последний элмент списка {lst[-1]}')
print(f'Элементы элмент со 2 по 4й {lst[2:5]}')

lst.remove("Python")

print(lst)



