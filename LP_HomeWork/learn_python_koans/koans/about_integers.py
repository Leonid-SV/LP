from koans_plugs import *


def test_can_sum_up():
    """
        Целые числа можно складывать
    """

    assert 1 + 1 == 2  # Вставьте вместо __ такое значение, чтобы оно совпадало с результатом выполнения 1 + 1

test_can_sum_up()

def test_can_deduct():
    """
        Целые числа можно вычитать
    """

    assert 32 - 11 == 21

test_can_deduct()

def test_can_multiply():
    """
        Целые числа можно умножать
    """

    assert 8 * 3 == 24

test_can_multiply()

def test_can_divide():
    """
        Целые числа можно делить.

        Обратите внимание, что в результате деления целых чисел можно получить вещественное число.
    """

    assert 5 / 2 == 2.5

test_can_divide()

def test_assign_to_variables():
    """
        Целые числа можно записывать в переменные.
    """
    x = 30
    assert x / 6 == 5.0

test_assign_to_variables()