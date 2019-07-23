import os
def chechLogined(iqn):
    cmd="iscsiadm -m session"
    try:
        logineds=os.popen(cmd).readlines()
        print logineds
    except Exception as e:
        print e
    re=0
    i=1
    for st in logineds:
        print "no "+str(i)+" "+st
        i=i+1
        if(st.find(iqn)>=0):
            re=1
    return re

if __name__ == '__main__':
    iqn="iqn.2003-01.org.linux-iscsi.iscsi.x8664:sn.0ae60ea0229d";
    re=chechLogined(iqn)
    print re