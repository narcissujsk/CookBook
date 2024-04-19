#!/usr/bin/python3

import logging
import threading
import requests
from bs4 import BeautifulSoup
from Image import Image
from lxml import etree
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        log.info("开始线程：" + self.name)
        self.download(self.threadID)
        log.info("退出线程：" + self.name)
        return

    def download(self, i):
        try:
            time.sleep(2)
            url = "https://wallhaven.cc/search?categories=111&purity=110&sorting=favorites&order=desc&ai_art_filter=1&page="
            url = url + str(self)
            log.info(url)
            payload = {}
            files = {}
            headers = {
            }
            response = requests.request("GET", url, headers=headers, data=payload, files=files)
            # print(response.text)
            soup = BeautifulSoup(response.content, 'lxml')
            # print(soup.title)
            print(soup.select(".preview"))
            pList = soup.select(".preview");
            for p in pList:
                href = p.get("href")
                log.info(href)
                href_response = requests.request("GET", href, headers=headers, data=payload, files=files)
                soup = BeautifulSoup(href_response.content, 'lxml')
                wallpaper = soup.select("#wallpaper")
                for paper in wallpaper:
                    image = Image(paper.get("src"))
                    image.download()
            log.info("  downloaded over")
        except Exception as e:
            log.error(e)
        return


if __name__ == "__main__":
    log.info("start")
    list = []
    for i in range(70, 80):
        thread = myThread(i, "thread" + str(i), 1)
        thread.start()
        list.append(thread)
    for thread in list:
        thread.join()
    log.info("end")

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
