import os
from glob import glob
# Connect-IscsiTarget -NodeAddress $Target.NodeAddress

#Get-IscsiTarget
#iqn.2003-01.org.linux-iscsi.localhost.x8664:sn.41046f9f6977
#iqn.2003-01.org.linux-iscsi.localhost.x8664:sn.691bed5e444f
#Disconnect-IscsiTarget -NodeAddress $Target.NodeAddress

def GetIscsiTarget():
    cmd = " Get-IscsiTarget  "
    with PowerShell() as ps:
        re = ps.run(cmd)
    return re


def SetInitiatorPort(NewNodeAddress):
    cmd=" Set-InitiatorPort -NodeAddress (Get-InitiatorPort).NodeAddress  -NewNodeAddress "+NewNodeAddress
    with PowerShell() as ps:
        re = ps.run(cmd)
    return re


def ConnectIscsiTarget(TargetNodeAddress):
    cmd=" Connect-IscsiTarget -NodeAddress  "+TargetNodeAddress
    with PowerShell() as ps:
        re = ps.run(cmd)
    return re

def DisconnectIscsiTarget(TargetNodeAddress):
    cmd=" Disconnect-IscsiTarget -NodeAddress  "+TargetNodeAddress+" -Confirm:$false"
    with PowerShell() as ps:
        re = ps.run(cmd)
    return re

class PowerShell:
    # from scapy
    def __init__( self, ):
        basecmd = self._where('PowerShell.exe')+ " -NoLogo -NonInteractive -Command "
        print (basecmd)
        self.basecmd=basecmd

    def __enter__( self ):
        return self

    def __exit__( self, a, b, c ):
        self.basecmd=''

    def run( self, cmd, timeout=15 ):
        b_cmd = self.basecmd+" \""+cmd+"\""
        print (b_cmd)
        try:
            re = os.popen(b_cmd).readlines()
            print (re)
        except Exception as e:
            print (e)
            re = ''
        return re

    @staticmethod
    def _where( filename, dirs=None, env="PATH" ):
        """Find file in current dir, in deep_lookup cache or in system path"""
        if dirs is None:
            dirs = []
        if not isinstance(dirs, list):
            dirs = [dirs]
        if glob(filename):
            return filename
        paths = [os.curdir] + os.environ[env].split(os.path.pathsep) + dirs
        try:
            return next(
                os.path.normpath(match) for path in paths for match in glob(os.path.join(path, filename)) if match)
        except (StopIteration, RuntimeError):
            raise IOError("File not found: %s" % filename)


if __name__ == '__main__':
    # Example:
    #SetInitiatorPort("iqn.2019-01.inspur.iscsi:sn.test")
    #re=GetIscsiTarget()
    re=DisconnectIscsiTarget("iqn.2003-01.org.linux-iscsi.localhost.x8664:sn.41046f9f6977")
    print(re)
        #'Get-NetAdapter