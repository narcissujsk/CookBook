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
target = 'https://6ff7076002cca9e4493c.bi17.cc/html/96018/list.html'
req = requests.get(url=target)
print(req.text)
div_bf = BeautifulSoup(req.text,'lxml')
div = div_bf.find_all('dd')
print(div)
names=[]
urls=[]
for i in div:
    print(i)
    print(i.text)
    names.append(i.text)
    urls.append(i.find_all('a')[0]['href'])
    print(i.find_all('a')[0]['href'])

print(names)
print(urls)

if __name__ == '__main__':
    print('start')


