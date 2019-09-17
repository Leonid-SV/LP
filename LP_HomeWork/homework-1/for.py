"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

import numpy as np

data = [
    {'school_class': '4a',
     'scores': [3, 4, 4, 5, 2]},
    {'school_class': '1a',
     'scores': [4, 5, 3, 3, 4]},
    {'school_class': '1b',
     'scores': [3, 5, 2, 5, 4]}
        ]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for classes in data:
        for scores in classes['scores']:
            print(scores)
            # class_avg = np.average(scores)
            pass
    
if __name__ == "__main__":
    main()
