# -*- coding:utf-8 -*-
import logging,base64
import sys

from Crypto.Cipher import AES
from sys import version_info
#pip uninstall crypto pycryptodome
#pip install pycryptodome
class PrpCrypt(object):

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            text = text + (b'\0' * add)
        elif count > length:
            add = (length - (count % length))
            text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为ascii字符
        re = base64.b64encode(self.ciphertext)
        return re

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        str = base64.standard_b64decode(text)
        plain_text = cryptor.decrypt(str)
        return plain_text.rstrip(b'\0')


if __name__ == '__main__':
    logging.basicConfig(
        filename='./log',
        level=logging.INFO,
        format='%(message)s'
    )
    if sys.version_info < (3, 0):
        print("2.7")
    else:
        print ("3.0")

    pc = PrpCrypt('keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt("testtesttest")  # 加密
    logging.info(e)
    d = pc.decrypt(e)  # 解密
    logging.info(d)
    print("1:", e)
    print("2:", d)

