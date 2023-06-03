import os,logging
def chechLogined(iqn):
    logging.basicConfig(
        filename='/root/iscsi.log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )
    cmd="iscsiadm -m session"
    try:
        logineds=os.popen(cmd).readlines()
        logging.info( logineds)
    except Exception as e:
        logging.error(e)
    re=0
    i=1
    for st in logineds:
        logging.info("no "+str(i)+" "+st)
        i=i+1
        if(st.find(iqn)>=0):
            re=1
    return re

if __name__ == '__main__':
    iqn="iqn.2003-10.01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    re=chechLogined(iqn)
    logging.info( re)