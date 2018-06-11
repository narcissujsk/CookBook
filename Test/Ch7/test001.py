import unittest
import Chapter7.P1
from Chapter7.P1 import *

class Test_make_elemet(unittest.TestCase):
    def test_make_elemet(self):
        print("make_elemet")
        re=make_elemet('item','value',size='13',name1='name1')
        print(re)
    def setUp(self):
        print("before")
    def tearDown(self):
        print("after")

class Test001(unittest.TestCase):
    def test001(self):
        re=add(1,2)
        print(re)
    def setUp(self):
        print("before")
    def tearDown(self):
        print("after")

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Test001)
    # 执行测试
    runner = unittest.TextTestRunner()
    re=runner.run(suite)
