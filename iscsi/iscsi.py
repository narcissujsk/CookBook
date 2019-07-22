import time,commands,json
import sys,os,daemon,subprocess
import logging
import os
import sys

import atexit
import signal

def daemonize(pidfile, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):

    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)   # Parent exit
    except OSError as e:
        raise RuntimeError('fork #1 failed.')

    os.chdir('/')
    os.umask(0)
    os.setsid()
    # Second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')

    # Flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()

    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    # Write the PID file
    fd = open(pidfile, 'w')
    fd.write('{}\n'.format(os.getpid()))
    fd.close()
    # Arrange to have the PID file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    import time
    while True:
        time.sleep(10)
        execute()


def log():
    logging.basicConfig(
        filename='/root/iscsi.log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )

def checkLogined(iqn):
    logging.debug("checkLogined : iscsiadm -m session")
    cmd="iscsiadm -m session"
    try:
        logineds=os.popen(cmd).readlines()
        logging.debug(logineds)
    except Exception as e:
        logging.info( e)
    re=0
    for st in logineds:
        logging.info(st)
        if(st.find(iqn)>=0):
            logging.debug("find "+iqn)
            re=1
    return re


def getMetadata():
    getMetadataCmd="curl http://169.254.169.254/openstack/latest/meta_data.json"
    cc = ''
    try:
        #p = subprocess.Popen(getMetadataCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        jsonstr=os.popen(getMetadataCmd).readline()
        #logging.info( p
        #jsonstr=p.stdout.readline()
        logging.info( str(jsonstr))
        cc=json.loads(str(jsonstr))
    except Exception as e:
        logging.info( e)
    return cc;



def login(initiatorName,ip,iqn):
    logging.info( "login in "+initiatorName +"  "+ip+"  "+iqn)
    #re = os.system('yum install iscsi-initiator-utils -y')
    cmd="echo 'InitiatorName="+initiatorName+"'>/etc/iscsi/initiatorname.iscsi"
    re = os.system(cmd)
    logging.info( cmd)
    logging.info( re)

    cmd="systemctl restart iscsid"
    re = os.system(cmd)
    logging.info( cmd)
    logging.info( re)

    cmd="iscsiadm -m discovery -t st -p "+ip
    re = os.system(cmd)
    logging.info( cmd)
    logging.info( re)

    cmd="iscsiadm -m node -T "+iqn+" -p "+ip+" --login"
    re = os.system(cmd)
    logging.info( cmd)
    logging.info( re)


def loginout(ip,iqn):
    logging.info( "login out "+ ip+"  " +iqn)
    cmd1="iscsiadm -m node -T "+iqn+" -p "+ip+" -u"
    #re = os.system(cmd1)
    logging.info( cmd1)
    re=subprocess.Popen(args=cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    re.communicate()
    logging.info( re)
    cmd2="iscsiadm -m node -T " + iqn + " -p " + ip + "  -o delete "
    #re = os.system(cmd2)
    logging.info( cmd2)
    #re = subprocess.call(cmd2)
    re = subprocess.Popen(args=cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    re.communicate()
    logging.info( re)
    re = os.system("systemctl restart iscsid")


def execute():
    re = getMetadata()
    logging.info("********************")
    meta = re['meta']
    logging.info( meta)
    iscsi = meta['iscsi']
    logging.info(iscsi)
    list = iscsi.split(',')
    logging.info( len(list))
    initiator_name = meta["initiator_name"]
    logging.info( initiator_name)
    for noi in list:
        logging.info( "****************************")
        logging.info( noi)
        noi_iqn = meta[noi + '_iqn']
        logging.info("iqn:"+ noi_iqn)
        noi_target = meta[noi + '_target']
        logging.info("target:" + noi_target)
        noi_status = meta[noi + "_status"]
        logging.info("action:" + noi_status)
        logging.info("*****************************")
        if (noi_status == "login"):
            if (checkLogined(noi_iqn)):
                logging.info( noi_iqn + " already logined")
            else:
                login(initiator_name, noi_target, noi_iqn)
        if (noi_status == "delete"):
            if (checkLogined(noi_iqn)):
                loginout(noi_target, noi_iqn)
            else:
                logging.info( noi_iqn + " are not logined")
    # loginout(ip,iqn)


if __name__ == '__main__':
    log();
    PIDFILE = '/root/daemon.pid'

    if len(sys.argv) != 2:
        logging.info(('Usage: {} [start|stop]'.format(sys.argv[0])))
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                      stdout='/root/daemon.log',
                      stderr='/root/daemon.log')
        except RuntimeError as e:
            logging.info(e)
            raise SystemExit(1)

        main()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            logging.info(('Not running'))
            raise SystemExit(1)

    else:
        logging.info(('Unknown command {!r}'.format(sys.argv[1])))
        raise SystemExit(1)