# -*- coding: utf-8 -*- 
import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')

if __name__ == "__main__":
    log.info("end")
    plist = ["%s:%s" % ("user", "keyold")]
    plist = ["root:%s" % "ppppp"]
    log.debug(" Change passwd for root plist : %s", plist)
    for line in plist:
        log.info(line)
        u, p = line.split(':', 1)
        log.info(u)
        log.info(p)
