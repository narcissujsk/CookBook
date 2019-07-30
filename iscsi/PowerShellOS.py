import os
from glob import glob



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
    with PowerShell() as ps:
        re = ps.run('ping 127.0.0.1')
        re = ps.run('Get-NetAdapter')
        #'Get-NetAdapter
    print('error:', os.linesep, re)