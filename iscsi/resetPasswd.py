import os,logging


def read_file(path):
    with open(path) as f:
        re=f.read()
    return re

if __name__ == '__main__':
    path="/root/CookBook/iscsi/key";
    try:
        os.remove('/root/CookBook/iscsi/key2')
    except Exception as e:
        ss = ''

    logging.basicConfig(
        filename='/root/CookBook/iscsi/key2',
        level=logging.INFO,
        format='%(message)s'
    )
    re=read_file(path)
    logging.info( re)