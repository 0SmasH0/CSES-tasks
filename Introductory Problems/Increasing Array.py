"""
https://cses.fi/problemset/task/1094/
"""

import time

number = int(input('Введите число: '))
lst = input('Введите список чисел: ').split()


def increasing_array(lst: list) -> int:
    elem = int(lst[0])
    moves = 0
    for i in lst[1:]:
        if int(i) < elem:
            moves += (elem - int(i))
        else:
            elem = int(i)

    return moves


start = time.time()

print(f'Минимальное количество ходов: {increasing_array(lst)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')