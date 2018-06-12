import unittest
import datetime

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def setUp(self):
        print ("ffff")


if __name__ == '__main__':
    unittest.main()
    print(datetime.datetime)
