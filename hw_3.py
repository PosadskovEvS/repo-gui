'''#task1
def div(dividend, divider):
    if divider == 0:
        return 'Error:division by zero'
    else:
        return dividend/divider


b = div(5, 0)
print(b)
'''

'''#task2
def resume(name,family,birth,city,email,phone):
    print(f'name - {name};family - {family};birth - {birth};city - {city};email - {email};phone - {phone}')


resume(family='Posadskov', name='Evgeny', birth='20.08.1993', city='Moscow', email = 'esposadskov@gmail.com', phone ='89290545222')
'''

'''#task3

def my_func(arg1, arg2, arg3):
    spisok = [arg1, arg2, arg3]
    spisok.sort(reverse=True)
    return spisok[0] + spisok[1]


print(my_func(1, 2, 3))
'''

'''#task4_1

def my_func(x, y):
    return x**y


print(my_func(5, 3))
'''
''' #task 4_2
def my_func(x, y):
    if y >= 0:
        a = 1
        for i in range(y):
             a *= x
        return a
    else:
        a = 1
        for i in range(-y):
             a *= x
        return 1 / a
print(my_func(2, -10))
'''

'''#task5 b - специальный символ прекращения работы программы

def sum_of_num():
    a = 0
    while True:
        str = input('Введите строку символов, разделенных пробелом: ')
        spisok = str.split()
        for i in spisok:
            if i == 'b':
                return a
            else:
                a += int(i)
    return a


print(sum_of_num())
'''

'''#task6_1

def int_func(text):
    return text.title()

print(int_func('я люблю сноуборд'))
'''
#tasks 6_2/ 7

def int_func(text):
    ind = 1
    str = ''
    for i in text:
        if ind == 1:
            str += i.upper()
        else:
            str += i
        if i == ' ':
            ind = 1
        else:
            ind = 0
    return str

print(int_func('сноуборд'))
print(int_func('я люблю сноуборд'))

