# 1. a)Створіть клас «Прямокутник», у якого є два поля (ширина і висота).
# b)Реалізуйте метод порівняння прямокутників за площею.
# c)Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі
# площ прямокутників, які ви складаєте).
# d) Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).

class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.width} rect1 {self.height}'

    # overloads methods of comparison operators
    def __gt__(self, other):
        return self.width * self.height > other.width * other.height

    def __lt__(self, other):
        return self.width * self.height < other.width * other.height

    def __ne__(self, other):
        return self.width * self.height != other.width * other.height

    def __ge__(self, other):
        return self.width * self.height >= other.width * other.height

    def __le__(self, other):
        return self.width * self.height <= other.width * other.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.width * self.height + other.width * other.height
        else:
            raise TypeError

    def __mul__(self, other: int):
        return (self.width * self.height) * other


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 4)

print(rect1 * 3)
print(rect2 + rect1)
print(rect1 > rect2)
print(rect1 < rect2)

# 2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та множення
# для екземплярів цього класу.


import math


class Rational:
    def __init__(self, a: int, b: int, c=None):
        self.a = a
        self.b = b
        if self.b == 0:
            raise ZeroDivisionError
        self.gcd = math.gcd(self.a, self.b)
        self.c = c


    def __str__(self):
        if self.c is None:
            return f"{self.a}/{self.b}"
        elif self.c == 0:
            return f"{self.a}/{self.b}"
        else:
            return f"{self.c} {self.a}/{self.b}"

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise NotImplemented
        if self.b == other.b:
            a = self.a + other.a
            b = self.b
        else:
            a = self.a * other.b + other.a * self.b
            b = self.b * other.b
        c = self.c
        if a >= b:
            c = a // b
            a %= b
        return Rational(a // self.gcd, b // self.gcd, c)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise NotImplemented
        if self.b == other.b:
            a = self.a - other.a
            b = self.b
        else:
            a = self.a * other.b - other.a * self.b
            b = self.b * other.b
        c = self.c
        if a < 0:
            c -= 1
            a += b
        return Rational(a // self.gcd, b // self.gcd, c)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise NotImplemented
        a = (self.c * self.b + self.a) * (other.c * other.b + other.a)
        b = self.b * other.b
        c = a // b
        a %= b
        return Rational(a // math.gcd(a, b), b // math.gcd(a, b), c)



#
    def mixed_value(self):
        return self.c + self.a / self.b

    def __lt__(self, other):
        return self.mixed_value() < other.mixed_value()

    def __le__(self, other):
        return self.mixed_value() <= other.mixed_value()

    def __eq__(self, other):
        return self.mixed_value() == other.mixed_value()

    def __ne__(self, other):
        return self.mixed_value() != other.mixed_value()

    def __gt__(self, other):
        return self.mixed_value() > other.mixed_value()

    def __ge__(self, other):
        return self.mixed_value() >= other.mixed_value()


x = Rational(a=1, b=3, c=2)
y = Rational(a=2, b=5, c=1)
res = x > y

print(res)


