class Person:
    def __init__(self, name):
        self.name = name

    # 把一个方法变成属性调用的
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('cannot delete attribute')


class SubPerson(Person):

    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print("setting name")
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete name')
        super(SubPerson, SubPerson).name.__delete__(self)


class NewPersiom(Person):
    @Person.name.getter
    def name(self):
        print('get new persion name')
        return super().name


if __name__ == '__main__':
    print('***********start*********')
    a = NewPersiom('name')
    print(a.name)
    a.name = '44'
    print(a.name)
    print('***********end*********')
