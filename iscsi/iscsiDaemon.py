import time,commands,json
import sys,os,daemon,subprocess


def checkLogined(iqn):
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


def getMetadata():
    getMetadataCmd="curl http://169.254.169.254/openstack/latest/meta_data.json"
    cc = ''
    try:
        #p = subprocess.Popen(getMetadataCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        jsonstr=os.popen(getMetadataCmd).readline()
        #print p
        #jsonstr=p.stdout.readline()
        print str(jsonstr)
        cc=json.loads(str(jsonstr))
    except Exception as e:
        print e
    return cc;



def login(initiatorName,ip,iqn):
    print "login in "+initiatorName +"  "+ip+"  "+iqn
    #re = os.system('yum install iscsi-initiator-utils -y')
    cmd="echo 'InitiatorName="+initiatorName+"'>/etc/iscsi/initiatorname.iscsi"
    re = os.system(cmd)
    print cmd
    print re

    cmd="systemctl restart iscsid"
    re = os.system(cmd)
    print cmd
    print re

    cmd="iscsiadm -m discovery -t st -p "+ip
    re = os.system(cmd)
    print cmd
    print re

    cmd="iscsiadm -m node -T "+iqn+" -p "+ip+" --login"
    re = os.system(cmd)
    print cmd
    print re


def loginout(ip,iqn):
    print "login out "+ ip+"  " +iqn
    cmd1="iscsiadm -m node -T "+iqn+" -p "+ip+" -u"
    #re = os.system(cmd1)
    print cmd1
    re=subprocess.Popen(args=cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    re.communicate()
    print re
    cmd2="iscsiadm -m node -T " + iqn + " -p " + ip + "  -o delete "
    #re = os.system(cmd2)
    print cmd2
    #re = subprocess.call(cmd2)
    re = subprocess.Popen(args=cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    re.communicate()
    print re
    re = os.system("systemctl restart iscsid")


def execute():
    re = getMetadata()
    print "********************"
    meta = re['meta']
    print meta
    iscsi = meta['iscsi']
    print iscsi
    list = iscsi.split(',')
    print len(list)
    initiator_name = meta["initiator_name"]
    print initiator_name
    for noi in list:
        print "****************************"
        print noi
        noi_iqn = meta[noi + '_iqn']
        print noi_iqn
        noi_target = meta[noi + '_target']
        print noi_target
        noi_status = meta[noi + "_status"]
        print noi_status
        print "*****************************"
        if (noi_status == "login"):
            if (checkLogined(noi_iqn)):
                print noi_iqn + " already logined"
            else:
                login(initiator_name, noi_target, noi_iqn)
        if (noi_status == "delete"):
            if (checkLogined(noi_iqn)):
                loginout(noi_target, noi_iqn)
            else:
                print noi_iqn + " are not logined"
    # loginout(ip,iqn)


if __name__ == '__main__':
    execute()