def f():
    try:
        v = input('Введите число от 1 до 10: ')
        print(10 + int(v))
    except:
        print('Введите именно число!')
        f()

f()


