'''
#task1
class Date:
    Date = ''
    def __init__(self, date):
        Date.Date = date
    @classmethod
    def get_number(cls):
        date_list = cls.Date.split('-')
        for i in range(len(date_list)):
            date_list[i] = int(date_list[i])
        Date.Date = date_list
        return f'Введенная дата: {Date.Date[0]}:{Date.Date[1]}:{Date.Date[2]}'
    @staticmethod
    def check():
        if Date.Date == '' or type(Date.Date) == str:
            Date.get_number()
        err = 0
        if Date.Date[0] < 0 or Date.Date[0] > 31:
            err = 1
            return f'Некорректно введено число'
        if Date.Date[1] < 1 or Date.Date[0] > 12:
            err = 1
            return f'Некорректно введен месяц'
        if Date.Date[2] < 1900 or Date.Date[2] > 2100:
            err = 1
            return f'Некорректно введен год'
        if err == 0:
            return f'Дата введена корректно'

a = Date('12-3-2022')
print(a.get_number())
print(a.check())
'''

'''
#task2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input('Введелите делимое: '))
b = int(input('Введите делитель: '))

try:
    if b == 0:
        raise OwnError('Ошибка! Вы пытаетесь разделить на ноль!')
    else:
        print(f'Result: {a/b}')
except OwnError as err:
    print(err)
'''
'''
#task3

class OwnException(Exception):
    def __init(self, err):
        self.err = err
inp = ''
list_numbers = list()
while inp != 'stop':
    inp = input('Введите число: ')
    if inp == 'stop':
        break
    try:
        if inp.isdigit() == False:
            raise OwnException('Вы ввели не число!')
    except OwnException as err:
        print(err)
    else:
        list_numbers.append(inp)
print(list_numbers)

'''

'''
# task 4, 5, 6
class Warehouse():
    Count = 0
    def __init__(self, name):
        print('Конструктор класса Warehouse')
        Warehouse.Count += 1
        self.name = name
        self.equipment = []
    def __str__(self):
        return f'Warehouse {self.name}'
    def add_eq(self, *equipments):
        for equipment in equipments:
            self.equipment.append(equipment)
            equipment.to_take(self)
    def get_info(self):
        print(f'Warehouse: {self.name}, the list pf equipment:')
        for i in self.equipment:
            print(i)

class Officeeq():
    def __init__(self, ink_level, paper, quant, deparment):
        self.ink_level = ink_level
        self.paper = paper
        self.depart = deparment
        try:
            self.quant = int(quant)
        except ValueError:
            print('В поле количество Вы ввели не числовое значение')
           # return f'В поле количество Вы ввели не числовое значение'
        else:
            self.quant = quant
    def __str__(self):
        return f'Ink level is {self.ink_level}, amount of paper in office equipment is {self.paper}, ' \
               f'quantity is {self.quant}'
    def to_take(self, warehouse):
        self.wh = warehouse
    def ch_dep(self, dep):
        self.depart = dep

class Printer(Officeeq):
    def __init__(self, ink_level, paper, quant, department, color):
        print('Конструктор класса Printer')
        Officeeq.__init__(self, ink_level, paper, quant, department)
        self.color = color
    def __str__(self):
        return f'Printer: color is {self.color}, quantity is {self.quant}, department is {self.depart}'
class Xerox(Officeeq):
    def __init__(self, ink_level, paper, quant, department, size):
        print('Конструктор класса Xerox')
        Officeeq.__init__(self, ink_level, paper, quant, department)
        self.size = size
    def __str__(self):
        return f'Xerox: size is {self.size}, quantity is {self.quant}, department is {self.depart}'

class Scanner(Officeeq):
    def __init__(self, ink_level, paper, quant, department, speed):
        print('Конструктор класса Scanner')
        Officeeq.__init__(self, ink_level, paper, quant, department)
        self.speed = speed
    def __str__(self):
        return f'Scanner: speed is {self.speed}, quantity is {self.quant}, department is {self.depart}'

wh1 = Warehouse('The first')
printer1 = Printer(100, 1000, 2, 'Sales', 'white')
xerox1 = Xerox(100, 1500, 23, 'Security', 'Big')
scanner1 = Scanner(100, 100, 7, 'Procurement', 'Fast')
wh1.add_eq(printer1, xerox1, scanner1)
wh1.get_info()
print(scanner1.wh)
print(xerox1.depart)
xerox1.ch_dep('Sales')
print(xerox1.depart)

'''
#task7

class ComplexNum():
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        return f'{self.re} + i*{self.im}'
    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)
    def __mul__(self, other):
        return ComplexNum(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)
a = ComplexNum(2, 3)
b = ComplexNum(5, 7)
c = ComplexNum(6, 8)
print(a)
print(b)
print(a+b)
print(a*b)
