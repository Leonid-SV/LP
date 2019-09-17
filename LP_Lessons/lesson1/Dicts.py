
new_d = {"city": "Москва", "temperature": "20"}
print(new_d['city'])
new_d['temperature'] = int(new_d['temperature']) + 5

print(new_d)

check = new_d.get('country')
print(check)

new_d['date'] = '27.05.2019'

print(f'длина списка {len(new_d)}')

new_d.update(date2 = '27.05.2019')

print(new_d)