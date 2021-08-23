from unittest import mock
import unittest

from  AESpswd import PrpCrypt


class Test_AESpawd(unittest.TestCase):

    def test01(self):
        print("")
        pc = PrpCrypt("qazwsxedcrfvtgby")  # 初始化密钥
        e = pc.encrypt("385152jsk1")  # 加密
        print(e)
        #9O+2O8xNiBYdKx1/RUrhlw==
        d = pc.decrypt(e)  # 解密
        print(d)
        print("1:", e)
        print("2:", d)

    def test02(self):
        print("")
        pc = PrpCrypt("qazwsxedcrfvtgby")  # 初始化密钥
        PrpCrypt.encrypt = mock.Mock(return_value="9O")
        e = pc.encrypt("385152jsk1")
        print(e)
        self.assertEqual(e, "9O")