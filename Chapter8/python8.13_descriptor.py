# Base class .Uses a descriptor to set a value

#NOT OVER
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# 强制类型的装饰器
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(' expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('expected>0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int

    def __repr__(self):
        return "Integer"


class Float(Typed):
    expected_type = float

    def __repr__(self):
        return "Float"


class UnsignedFloat(Integer, Unsigned):
    pass


class String(Typed):
    expected_type = str

    def __repr__(self):
        return "String"


class SizedString(String, MaxSized):
    def __repr__(self):
        return "SizedString"

    pass


class Stock:
    name = SizedString('name', size=8)
    age = Integer('age')

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __repr__(self):
        return "age=" + str(self.age) + " name=" + self.name


# 可以使用一些技术简化在类中设置约束的步骤
# 类装饰器
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            print(value)
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value)
        return cls

    return decorate


@check_attributes(name=SizedString(size=8), age=Integer())
class Stock1:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __repr__(self):
        return "age=" + str(self.age) + " name=" + self.name


if __name__ == '__main__':
    def t1():
        p = Stock1("sss", 99)
        print(p)
        p.name = '01234567'
        p.age = 3
        print(p)

    #t1()

    def t2():
        p = Stock("sss", 99)
        print(p)
        p.name = '01234567'
        p.age = 3.0
        print(p)
    t2()

