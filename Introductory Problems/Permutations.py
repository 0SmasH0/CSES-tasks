"""
https://cses.fi/problemset/task/1070/
"""

import time

number = int(input('Введите число: '))


def permutations(num: int) -> str | list:
    if num in [2, 3]:
        return "NO SOLUTION"
    else:
        even = list(range(2, num + 1, 2))
        odd = list(range(1, num + 1, 2))
        res = even + odd
        return res


start = time.time()

print('Результат:', *permutations(number))

end = time.time()

print(f'Время выполнения программы: {end - start}')
