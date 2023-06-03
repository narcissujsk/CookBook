class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # 把一个方法变成属性调用的
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot delete attribute')


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    a = Person('name')
    print(a.first_name)
    a.first_name = '44'
    print(a.first_name)
    # del a.first_name
    c = Circle(4.9)
    print(c.area)
    print(c.perimeter)
