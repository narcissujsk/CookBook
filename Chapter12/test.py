import os


def login(initiatorName,ip,iqn):
    re = os.system('yum install iscsi-initiator-utils -y')
    re = os.system(
        "echo 'InitiatorName="+initiatorName+"'>/etc/iscsi/initiatorname.iscsi")
    re = os.system("systemctl restart iscsid")
    re = os.system("iscsiadm -m discovery -t st -p "+ip)
    re = os.system(
        "iscsiadm -m node -T "+iqn+" -p "+ip+" --login")


def loginout(ip,iqn):
    re = os.system("iscsiadm -m node -T "+iqn+" -p "+ip+" -u")
    re = os.system("iscsiadm -m node -T " + iqn + " -p " + ip + "  -o delete ")
    re = os.system("systemctl restart iscsid")


if __name__ == '__main__':
    initiatorName="iqn.2003-10.01.org.linux-iscsi.localhost.x8664:sn.691bed5e444f.client";
    ip="192.168.195.172";
    iqn="iqn.2003-10.01.org.linux-iscsi.localhost.x8664:sn.691bed5e444f";
    login(initiatorName,ip,iqn)
    #loginout(ip,iqn)