
'''#task1
from sys import argv

script_name, production, rate, award = argv

print('Объем выработки: ', production)
print('Ставка: ', rate)
print('Премия: ', award)
print('Ваша заработная плата составляет: ', int(production)*int(rate)+int(award))
'''

'''#task2

base = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = list()
new_list.append(base[0])
a = base[0]
for el in base:
    if el > a:
        new_list.append(el)
    a = el
print(new_list)
'''

'''#task 3

new_list = [i for i in range(20, 241, 1) if i % 20 == 0 or i % 21 == 0]

print(new_list)
'''
'''#task 4
base = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in base if base.count(el) == 1]
print(new_list)
'''

'''#task5
from functools import reduce

def my_func(arg1, arg2):
    return arg1 * arg2


new_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, new_list))
'''

'''#task6_1

from itertools import count, cycle

a = int(input('Введите начальное число последовательности: '))
b = int(input('Введите порог окончания цикла: '))
for el in count(a):
    if el > b:
        break
    else:
        print(el)
#task6_2
c = 0
for el in cycle('Evgeny'):
    if c > 10:
        break
    print(el)
    c += 1
'''
#task7

from itertools import count
from math import factorial


def fact(n):
    for el in count(1):
        if el > n:
            break
        else:
            yield factorial(el)

for el in fact(10):
    print(el)
