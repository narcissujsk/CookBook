# -*- coding:utf-8 -*-
import logging,base64
import sys
import os,logging
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
        print(key)
        print(type(key))
        print(len(key))
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。


def read_file(path):
    if os.path.exists(path):
        with open(path) as f:
            re=f.read()
    return re.strip().replace("\r", "")


def write(file,text):
    fd = open(file, 'w')
    fd.write('{}\n'.format(text))
    fd.close()

def reset_passwd(passwd):
    cmd="echo root:"+passwd+" | chpasswd"
    print(cmd)
    #re = os.popen(cmd).readlines()
    return 0


if __name__ == '__main__':

    try:
        os.remove('/root/CookBook/iscsi/log')
    except Exception as e:
        ss = ''
    logging.basicConfig(
        filename='/root/CookBook/iscsi/log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )
    passwdpath="/root/CookBook/iscsi/passwd";
    keypath = "/root/CookBook/iscsi/key";
    aespasswd = read_file(passwdpath)
    oldkey = read_file(keypath)
    oldpc = PrpCrypt(oldkey)  # 初始化密钥
    print(oldkey)
    logging.info(oldkey)
    oldpasswd = oldpc.decrypt(aespasswd)

    print("old aespasswd:"+aespasswd)
    print("old key:"+oldkey)
    print(len(oldkey))
    print("old passwd:" + oldpasswd)
    reset_passwd(oldpasswd)