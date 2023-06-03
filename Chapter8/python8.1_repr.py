class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__的标准做法是使他产生的字符串满足eval(repr(x))===x
    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


if __name__ == '__main__':
    print("start")
    p = Pair(3, 4)
    print(repr(p))
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))
    p2 = eval(repr(p))
    print("p2:")
    print(p2)
    if eval(repr(p)) == p:
        print("OK")
