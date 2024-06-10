"""
https://cses.fi/problemset/task/1069/
"""

import time

dna = input('Введите строку: ')


def repetitions(dna: str):
    length = len(dna)

    if length == 1:
        return 1

    elem = dna[0]
    our_max_length = []
    length_elems = 1

    for i in dna[1:]:
        if elem == i:
            length_elems += 1
        else:
            elem = i
            our_max_length.append(length_elems)
            length_elems = 1
    else:
        our_max_length.append(length_elems)

    return max(our_max_length)


start = time.time()

print(f'Максимальная длина подстроки: {repetitions(dna)}')

end = time.time()

print(f'Время выполнения программы: {end - start}')
