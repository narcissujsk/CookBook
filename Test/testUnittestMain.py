import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def myTestCase(self):
        self.assertEqual(True, True)
        print("myTestCase")
    def setUp(self):
        print ("ffff")


if __name__ == '__main__':
    unittest.main()
