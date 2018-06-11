# -*-coding:utf-8-*-
from  urllib import request
from bs4 import  BeautifulSoup
url="http://www.baidu.com"
req=request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36")
resp=request.urlopen(req)
print(resp.read().decode("utf-8"))
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36