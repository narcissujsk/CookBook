import logging
import logging
import threading
import requests
from bs4 import BeautifulSoup
from Image import Image
from lxml import etree
import time

# # pip install lxml

logging.config.fileConfig('./logging.conf')
# 创建 logger
logger = logging.getLogger('root')

from Image import Image

url = 'https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png'

logger.info(url)
if __name__ == "__main__":
    logger.info("end")
