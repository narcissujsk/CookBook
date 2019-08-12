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
    def encrypt( self, text ):
        cryptor = AES.new(self.key, self.mode, IV.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext).decode('utf8')

    # 解密函数
    def decrypt( self, text ):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text).decode('utf8')

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。


if __name__ == '__main__':
    logging.basicConfig(
        filename='./log',
        level=logging.INFO,
        format='%(message)s'
    )
    pc = PrpCrypt("qazwsxedcrfvtgby")  # 初始化密钥
    e = pc.encrypt("385152jsk1")  # 加密
    logging.info(e)
    d = pc.decrypt(e)  # 解密
    logging.info(d)
    print("1:", e)
    print("2:", d)

