# -*- coding: utf-8 -*-

"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def ask_user():
    """
    Замените pass на ваш код
    """
    q_a = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты коммунист?": "Нет, я парикмахер."}

    try:
        q = input("Спрашивай, не стесняйся: ")
        if q in q_a:
            print(q_a[q])
        else:
            print('Вопрос не понятен')
            ask_user()

    except (KeyboardInterrupt, EOFError):
        print("Пока!")


if __name__ == "__main__":
    ask_user()
