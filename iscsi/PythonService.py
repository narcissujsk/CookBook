# ZPF
# encoding=utf-8
import win32timezone
from logging.handlers import TimedRotatingFileHandler
import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect
import time
import shutil


class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService"                    #服务名
    _svc_display_name_ = "PythonService"                 #job在windows services上显示的名字
    _svc_description_ = "PythonService"        #job的描述

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.path = 'C:\\WebSite'
        self.T = time.time()
        self.run = True

    def _getLogger(self):
        '''日志记录'''
        logger = logging.getLogger('[PythonService]')
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        if os.path.isdir('%s\\log'%dirpath):  #创建log文件夹
            pass
        else:
            os.mkdir('%s\\log'%dirpath)
        dir = '%s\\log' % dirpath

        handler = TimedRotatingFileHandler(os.path.join(dir, "Clearjob.log"),when="midnight",interval=1,backupCount=20)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        self.logger.info("service is run....")
        try:
            while self.run:
                self.logger.info('---Begin---')

                self.logger.info('---End---')
                time.sleep(10)

        except Exception as e:
            self.logger.info(e)
            time.sleep(60)

    def SvcStop(self):
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)