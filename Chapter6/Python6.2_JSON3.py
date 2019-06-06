# -*- coding: utf-8 -*- 
import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")
print("dd")

import requests


i = 1
while i <= 10:
    i += 1
    log.info(i)
    time.sleep(1) # 休眠6秒
    try:
        r = requests.get('https://github.com/timeline.json')
    except Exception as e:  # 只能通过这个异常处理，Exception 抓住所有的异常
      print(e)
    else:
        rr = r.json()
        i=11

log.info(rr)

if __name__ == "__main__":
    log.info("end")
