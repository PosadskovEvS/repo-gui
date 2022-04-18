'''#task1
import time
import sys

class TrafficLight:
    __color = ''

    def runniing(self, color):
        print('Запуск светофора')

        if self.__color == '':
            if color == 'Red':
                self.__color = color
                print(color)
                time.sleep(7)
            else:
                print('Error: Color should be red')
                sys.exit()
        elif self.__color == 'Red':
            if color == 'Yellow':
                self.__color = color
                print(color)
                time.sleep(2)
            else:
                print('Error: Color should be yellow')
                sys.exit()
        elif self.__color == 'Yellow':
            if color == 'Green':
                 self.__color = color
                 print(color)
                 time.sleep(15)
            else:
                 print('Error: Color should be green')
                 sys.exit()
        elif self.__color == 'Green':
            if color == 'Red':
                self.__color = color
                print(color)
                time.sleep(7)
            else:
                print('Error: Color should be red')
                sys.exit()

a = TrafficLight()
a.runniing('Red')
a.runniing('Green')
a.runniing('Red')
'''

'''#task2

class Road:
    def __init__(self, length, width):
        self.__lenth = length
        self.__width = width

    def weight(self, w_s, q_s):
        return self.__lenth * self.__width * w_s * q_s

a = Road(20, 5000)
print(a.weight(25, 5))
'''


'''#task3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._Worker__income.get('wage') + self._Worker__income.get('bonus')


a = Position('Evgeni', 'Posadskov', 'Cheif Expert', {'wage': 100000, 'bonus': 50000})
print(f'Полное имя: {a.get_full_name()}')
print(f'Общее вознаграждение: {a.get_total_income()}')
b = Position('Ivan', 'Ivanov', 'Expert', {'wage': 200000, 'bonus': 50000})
print(f'Полное имя: {b.get_full_name()}')
print(f'Общее вознаграждение: {b.get_total_income()}')
'''
'''
#task4

class Car:
    def __init__(self, speed, color, name, ispolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')
    def show_speed(self):
        return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name, ispolice):
        super().__init__(speed, color, name, ispolice)

class WorkCar(Car):
    def __init__(self, speed, color, name, ispolice):
        super().__init__(speed, color, name, ispolice)
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости, ваша скорость: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, ispolice):
        super().__init__(speed, color, name, ispolice)
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости, ваша скорость: {self.speed}')

class Police(Car):
    def __init__(self, speed, color, name, ispolice):
        super().__init__(speed, color, name, ispolice)

a = TownCar(78,'Black','Kia',False)
a.go()
a.show_speed()
a.turn('Right')
a.stop()
b = WorkCar(35,'White', 'Bmw', False)
b.show_speed()
'''
#task 5
class Stationery:
    title = 'Stationery'
    def draw(self):
        print(f'Родительский метод класса Stationery')

class Pen:
    def draw(self):
        print('Родительский метод класса Pen')
class Pencil:
    def draw(self):
        print('Родительский метод класса Pencil')
class Handle:
    def draw(self):
        print('Родительский метод класса Handle')

s = Stationery()
s.draw()
p = Pen()
p.draw()
pn = Pencil()
pn.draw()
h = Handle()
h.draw()


