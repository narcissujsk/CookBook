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
        download(self.threadID)
        log.info("退出线程：" + self.name)


def download(i):
    url = "https://wallhaven.cc/search?categories=111&purity=110&sorting=favorites&order=desc&ai_art_filter=1&page="
    url = url + str(i)
    log.info(url)
    payload = {}
    files = {}
    headers = {
    }
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    # print(response.text)
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.title)
    # print(soup.select(".preview"))
    pList = soup.select(".preview");
    for p in pList:
        href = p.get("href")
        href_response = requests.request("GET", href, headers=headers, data=payload, files=files)
        soup = BeautifulSoup(href_response.content, 'lxml')
        wallpaper = soup.select("#wallpaper")
        for paper in wallpaper:
            image = Image(paper.get("src"))
            image.download()
    time.sleep(1000)


if __name__ == "__main__":
    log.info("end")
    for i in range(11,20):
        thread1 = myThread(i, "thread" + str(i), 1)
        thread1.start()
    while True:
        time.sleep(1000)
