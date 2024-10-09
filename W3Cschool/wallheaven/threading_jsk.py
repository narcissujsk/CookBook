#!/usr/bin/python3

import logging
import threading
import requests
from bs4 import BeautifulSoup
from Image import Image
from lxml import etree
import time
import requests
from bs4 import BeautifulSoup
from Image import Image
from lxml import etree
import os
import threading
# # pip install lxml

logging.config.fileConfig('./logging.conf')
# 创建 logger
logger = logging.getLogger('root')


class myThread(threading.Thread):
    def __init__(self, num, name, delay):
        threading.Thread.__init__(self)
        self.num = num
        self.name = name
        self.delay = delay

    def run(self):
        logger.info("开始线程：" + self.name)
        self.downs(self.num)

        logger.info("退出线程：" + self.name)
    def downs(self, i):
        url = "https://wallhaven.cc/search?categories=111&purity=001&sorting=favorites&order=desc&ai_art_filter=1&page=" + str(
            i)

        payload = {}
        files = {}
        cookie = "pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1727659593%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3Dwallhaven.cc%26rsv_spt%3D1%26rsv_iqid%3D0xce98b8730040e8c4%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dmaxthon2%26rsv_dl%3Dtb%26rsv_enter%3D0%26rsv_btype%3Dt%26inputT%3D3110%26rsv_t%3DcaefxYS2GRQPAfxAktjx%2F9k%2F14tCXWCguxaL3e60PooSbDCtSpMpJXElgddsLTE%26rsv_sug3%3D14%26rsv_sug1%3D13%26rsv_sug7%3D100%26oq%3Dwallhaven%26rsv_pq%3De953d8d900b67bf6%26rsv_sug4%3D4750%22%5D; _pk_id.1.01b8=2bd4be076d096303.1727659593.; _pk_ses.1.01b8=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IktUcmoxUzRQZmJBTnM4SVB1UHZvaWc9PSIsInZhbHVlIjoiendkVEtqNmd3bVh2SnFIcWVTekZObE04MjIzQVRKWWh6TzlobnVKWm5hc2c2UFwvdkdlT3Yxb3dPVzAyQ3pOdExPZWdcL1pKUFwvU01xNjJRdTF3eklRSEJ4dVNhV01WbE1SS2pFZ0ZTZzYweGtQVGU4RCs0THpcLytVSHp4Y05VU1VKYUJoekpiUG9aT3ZDeW00dUZueTM5SjEwZGNWd1h1c3BYQWhzdWxyWDBUZz0iLCJtYWMiOiI1MmU2ZGY5NTJlMjJmNjA4YmZkZDNhMWRmMmVmZGJmNjBjYWY3ZWI3YjIyMjE5MGRjN2FlZjA5YjM2ZTdmNzNlIn0%3D; XSRF-TOKEN=eyJpdiI6Imh3TVVJdHZ1YVkramxaRDBCK1lKRlE9PSIsInZhbHVlIjoiXC83OVpSd2dab1E2eGpzWGdQd3BrTFc1V1FpK2hGU2o0V1VhaGlNekxBUlg5OVFoUXFCV0xYZ2gxSlRIWVJIN1AiLCJtYWMiOiIyM2RhZDU0ZTE4MjJlZmFhZGZkOGY5OTczNjc2YWQ4NjdjZmQ2MWMyZDllZGU4MWVkYmE0NmYyNjUxZDcwMDYwIn0%3D; wallhaven_session=eyJpdiI6IkZGb3ZwV3hHR0FXbzY5Rjk0TkFBSHc9PSIsInZhbHVlIjoiTVZablVxNWJuRDVneHNKcGhMTmhyNFFabWliTm4xR0dWM1hMc2dKUmY2cGx6RXlBYWI1QXJwdnJOVTh3dUZDZCIsIm1hYyI6IjY5NzUwODY0NDZjYmE1OGFlOTY5NzE5NDAzNTcyNDhjZThkZDgyMjI5Mzg1MDY0OTBhMDhiNDBmMDU0Mzk5YmUifQ%3D%3D"

        headers = {
        "cookie": cookie
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

    # print(response.text)
        soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.title)
    # print(soup.select(".preview"))
        pList = soup.select(".preview");
        for p in pList:
            logger.info(p.get("href"))
            href = p.get("href")
            href_response = requests.request("GET", href, headers=headers, data=payload, files=files)
            soup = BeautifulSoup(href_response.content, 'lxml')
            wallpaper = soup.select("#wallpaper")
            for paper in wallpaper:
                image = Image(paper.get("src"), i)
                image.download()


if __name__ == "__main__":
    logger.info("start")
    list = []
    for i in range(1, 15):
        thread = myThread(i, "thread" + str(i), 1)
        thread.start()
    time.sleep(99999)
    logger.info("end")

# thread21 = myThread(21, "thread21" , 1)
# thread21.start()
# thread22 = myThread(22, "thread22" , 1)
# thread22.start()
# thread23 = myThread(23, "thread23" , 1)
# thread23.start()
# thread24 = myThread(24, "thread24" , 1)
# thread24.start()
# thread25 = myThread(25, "thread25" , 1)
# thread25.start()
# thread21.join()
# thread22.join()
# thread23.join()
# thread24.join()
# thread25.join()
