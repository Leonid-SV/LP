price = 100
discount = 5

def get_summ(one, two, delimiter='&'):
    answ = ''.join([str(one), str(delimiter),
                    str(two)]).upper()
    return answ

print(get_summ('Learn', 'python'))


