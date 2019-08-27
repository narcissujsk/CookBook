# -*- coding:utf-8 -*-
import logging,base64
import sys

from Crypto.Cipher import AES
from sys import version_info
#pip uninstall crypto pycryptodome
#pip install pycryptodome

AES_SECRET_KEY = '1234567812345678' #此处16|24|32个字符
IV = "1234567890123456"
# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class PrpCrypt(object):

    # 加密函数
    def encrypt2( self, text ):
        cryptor = AES.new(self.key, self.mode, IV.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext)

    # 解密函数
    def decrypt2( self, text ):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text)

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
    pc = PrpCrypt(AES_SECRET_KEY)  # 初始化密钥
    e = pc.encrypt2("testtesttest")  # 加密
    logging.info(e.decode('utf8'))
    d = pc.decrypt2(e.decode('utf8'))  # 解密
    logging.info(d.decode('utf8'))
    print("1:", e.decode('utf8'))
    print("2:", d.decode('utf8'))

