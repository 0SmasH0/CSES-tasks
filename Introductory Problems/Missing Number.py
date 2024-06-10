"""
https://cses.fi/problemset/task/1083/
"""

import time

number = int(input('Введите число: '))
lst = input('Введите список чисел: ').split()


def missing_num(num: int, lst: list):
    suma = 0
    for i in lst:
        suma += int(i)

    end_suma = sum(list(range(1, num + 1)))

    return end_suma - suma


start = time.time()

print(f'Результат: {missing_num(number, lst)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
