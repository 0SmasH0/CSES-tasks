"""
https://cses.fi/problemset/task/1068/
"""

import time

number = int(input('Введите число: '))


def weird_algo(num: int) -> None:
    while True:
        print(num, end=' ')
        if num == 1:
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1


start = time.time()

weird_algo(number)

end = time.time()

print(f'\nВремя выполнения программы: {end - start}')
