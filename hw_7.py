'''# task1

class Matrix:
    def __init__(self, list):
        self.list = list
    def __str__(self):
        return f'{self.list}'

    def __add__(self, other):
        result = self.list
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                result[i][j] = self.list[i][j] + other.list[i][j]
        return Matrix(result)

a = Matrix([[1, 2], [2, 4]])
b = Matrix([[1, 2], [2, 4]])
print(a+b)
'''

'''#task2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        print('Конструктор родительского класса Clothes')
    @abstractmethod
    def cons(self):
        pass
class Coat(Clothes):
    def __init__(self, v):
        self.V = v
    @property
    def cons(self):
        return self.V/6.5 + 0.5
class Suit(Clothes):
    pass
    def __init__(self, h):
        self. H = h
    def cons(self):
        return self.H * 2 + 0.3

a = Suit(5)
print(a.cons())
b = Coat(48)
print(b.cons)
'''

#task3


class Cage:
    def __init__(self, q):
        self.q = q
    def __add__(self, other):
        return Cage(self.q + other.q)
    def __mul__(self, other):
        return Cage(self.q * other.q)
    def __sub__(self, other):
        if (self.q - other.q) > 0:
            return Cage(self.q - other.q)
        else:
            return f'Разница между объктами класса <= 0'
    def __floordiv__(self, other):
        return Cage(self.q // other.q)
    def __str__(self):
        return f'Объект класса Cage с параметром {self.q}'
    def make_order(self,step):
        count = self.q // step
        rest = self.q % step
        a = str()
        for i in range(count):
            a += step * '*' + '\n'
        a = a + rest * '*'
        return a


c1 = Cage(50)
c2 = Cage(10)
print(c1+c2)
print(c1*c2)
print(c1-c2)
print(c2-c1)
print(c1//c2)
print(c1.make_order(9))


