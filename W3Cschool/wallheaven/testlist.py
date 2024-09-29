import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")
import requests
from bs4 import BeautifulSoup
from Image import Image
from lxml import etree
logging.config.fileConfig('./logging.conf')
# 创建 logger
logger = logging.getLogger('root')

for i in range(1, 10):
    url = "https://wallhaven.cc/search?categories=111&purity=110&sorting=favorites&order=desc&ai_art_filter=1&page="+str(i)

    payload = {}
    files = {}
    headers = {
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

#print(response.text)
    soup = BeautifulSoup(response.content, 'lxml')
#print(soup.title)
#print(soup.select(".preview"))
    pList = soup.select(".preview");
    for p in pList:
        logger.info(p.get("href"))
        href=p.get("href")
        href_response = requests.request("GET", href, headers=headers, data=payload, files=files)
        soup = BeautifulSoup(href_response.content, 'lxml')
        wallpaper = soup.select("#wallpaper")
        for paper in wallpaper:
            image=Image(paper.get("src"),i)
            image.download()

if __name__ == "__main__":
    log.info("end")
