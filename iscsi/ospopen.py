import os,logging
if __name__ == '__main__':
    iqn="iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    cmd="echo root:385152jsk1 | chpasswd"
    re = os.popen(cmd).readlines()
    print(re)
