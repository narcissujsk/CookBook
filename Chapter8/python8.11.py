import math
class Structure:
    _field = []

    def __init__(self, *args):
        if len(args) != len(self._field):
            print("args number wrong")
        else:
            print('init')
            for name ,value in zip(self._field,args):
                setattr(self,name,value)



if __name__=='__main__':
    class Point(Structure):
        _field = ['x','y']

    class Circle(Structure):
        _field = ['radius']
        def area(self):
            return math.pi*self.radius**2

    p=Point(2,3)
    print(p.x)
    c=Circle(4)
    print(c.area())