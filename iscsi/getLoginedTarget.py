import os,logging
def getLogined():
    logging.basicConfig(
        filename='/root/iscsi.log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )
    cmd="iscsiadm -m session -P 1|grep Target"
    try:
        logineds=os.popen(cmd).readlines()
        logging.info( logineds)
    except Exception as e:
        logging.error(e)
    list=[]
    for st in logineds:
        noi=st[st.index(":")+1:st.index("(")].strip()
        list.append(noi)
    return list

if __name__ == '__main__':
    iqn="iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    tList=getLogined()
    logging.info( tList)