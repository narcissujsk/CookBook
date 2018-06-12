import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("test")
log.info("i")

import requests
from urllib import request, parse
from pprint import pprint

url = 'http://httpbin.org/post'


def use_request():
    params = {
        'name': 'name',
        'id': 'id'
    }

    querystring = parse.urlencode(params)
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36"
        , 'Spam': 'Eggs'
    }
    req = request.Request(url, querystring.encode('ascii'), headers=headers)
    u = request.urlopen(req)
    resp = u.read().decode("utf-8")
    print(resp)



def use_requests():
    params = {
        'name': 'name',
        'id': 'id'
    }

    querystring = parse.urlencode(params)
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36"
        , 'Spam': 'Eggs'
    }
    reqs = requests.post(url, querystring.encode('ascii'), headers=headers)
    text=reqs.text
    print(text)


def head_requests():
    resp=requests.head('http://www.python.org/index.html')
    status=resp.status_code
    print(resp.headers['content-type'])
    print(resp.headers['content-length'])
    print(resp.headers['last-modified'])


if __name__ == "__main__":
    log.info("yy")
    head_requests()