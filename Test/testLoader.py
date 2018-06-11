import unittest


class TestCase1(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    def test1(self):
        print("testCase1:test1")


    def test2(self):
        print("testCase1:test2")



class TestCase2(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    def test1(self):
        print("testCase2:test1")

    def test2(self):
        print("testCase2:test2")


if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)

