import os,logging
if __name__ == '__main__':
    iqn="iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    cmd="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\PowerShell.exe  -NoLogo -NonInteractive -Command \"& ping 127.0.0.1\""
    re = os.popen(cmd).readlines()
    print(re)