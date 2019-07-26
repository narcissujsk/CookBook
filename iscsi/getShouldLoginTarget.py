import os,logging

logging.basicConfig(
    filename='/root/iscsi.log',
    level=logging.INFO,
    format='%(levelname)s:%(asctime)s:%(message)s'
)

if __name__ == '__main__':
    iqn="iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d,iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    tList=iqn.split(",")
    logging.info( tList)