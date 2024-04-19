# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys
import logging
import threading
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

import requests

if __name__ == '__main__':
    target = 'https://6ff7076002cca9e4493c.bi17.cc/html/96018/1.html'
    req = requests.get(url=target)
    print(req.text)
    div_bf = BeautifulSoup(req.text,'lxml')

