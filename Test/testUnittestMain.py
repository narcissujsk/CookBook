import unittest
import datetime

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("end")

    def setUp(self):
        print ("setUp")

    def tearDown(self):
        # 测试用例执行完后所需执行的操作
        print("tearDown")


if __name__ == '__main__':
    unittest.main()
