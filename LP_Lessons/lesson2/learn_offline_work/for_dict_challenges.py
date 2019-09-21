# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
]

def name_counter(s):

    n_counts = {}

    for persons in s:
        x = persons['first_name']
        if x in n_counts:
            n_counts[x] += 1
        else:
            n_counts[x] = 1

    return n_counts

print('1. *******************')
for name, value in name_counter(students).items():
    print('Количество повторений имени {} : {}'.format(name, value))

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Егор'},

]

def find_max_rep(s):

    c = name_counter(s)

    max_rep = 0

    max_rep_name = ''

    for key, value in c.items():
        if value > max_rep:
            max_rep = value
            max_rep_name = key

    return max_rep_name

print('2. *******************')
print(f'Часто повторяющееся имя: { find_max_rep(students) }')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Петр'},
    {'first_name': 'Вася'},

  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


print('3. *******************')
c_count = 0
for group in school_students:

    max_rep_group_name = find_max_rep(group)
    c_count += 1
    print(f'Самое частое имя в Классе №{c_count}: {max_rep_group_name}')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {
      'class': '2a',
      'students': [
                  {'first_name': 'Маша'},
                  {'first_name': 'Оля'}
                    ]
  },
  {
      'class': '3c',
      'students': [
                  {'first_name': 'Олег'},
                  {'first_name': 'Миша'}
                    ]
  },
        ]

is_male = {   'Маша': False,   'Оля': False,   'Олег': True,   'Миша': True, }

def boys_girls_counter(some_school):

    school_bg_count = []

    for group in some_school:

        s_group =   {
                    'gruppa': group['class'],
                    'n_boys': 0,
                    'n_girls': 0,
                    }

        for person in group['students']:
            if person['first_name'] in is_male:
                if is_male[person['first_name']]:
                    s_group['n_boys'] += 1
                else:
                    s_group['n_girls'] += 1

        cl =    s_group['gruppa']
        g_cl =  s_group['n_girls']
        b_cl =  s_group['n_boys']

        school_bg_count.append({
                        'class':    cl,
                        'n_girls':  g_cl,
                        'n_boys':   b_cl,
                        })

    return school_bg_count


print('4. *******************')
sbc = boys_girls_counter(school)
for group in sbc:
    cl =    group['class']
    g_cl =  group['n_girls']
    b_cl =  group['n_boys']
    print(f'В классе {cl}: {g_cl} девочки и {b_cl} мальчика')

#???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
          {
              'class': '2a',
              'students': [
                          {'first_name': 'Маша'},
                          {'first_name': 'Оля'}
                          ]
          },
          {
              'class': '3c',
              'students': [
                          {'first_name': 'Олег'},
                          {'first_name': 'Миша'}
                          ]
          },
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

school_bg = boys_girls_counter(school)


group_max_boys = {
                        'class': '',
                        'n_boys': 0
                        }
group_max_girls = {
                        'class': '',
                        'n_girls': 0
                        }


print('5. *******************')
# print(school_bg)

for group in school_bg:

    if group['n_girls'] > group_max_girls['n_girls']:
        group_max_girls['n_girls'] = group['n_girls']
        group_max_girls['class'] = group['class']

    if group['n_boys'] > group_max_boys['n_boys']:
        group_max_boys['n_boys'] = group['n_boys']
        group_max_boys['class'] = group['class']

print('Больше всего мальчиков в классе {}'.format(group_max_boys['class']))
print('Больше всего девочек в классе {}'.format(group_max_girls['class']))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a