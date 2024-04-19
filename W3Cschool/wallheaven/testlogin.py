import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")



import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36 Edg/123.0.0.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

form_data = {
    'username': '1791121094@qq.com',
    "password": '3'
}

response = requests.post('https://wallhaven.cc/auth/login', data=form_data, headers=headers)
log.info(response)
log.info("********************headers********************")
headers1=response.headers
log.info(headers1)
listH=headers1.items()
for i in listH:
    log.info(i)
log.info("********************headers********************")
log.info("********************cookies********************")
cookies=response.cookies
log.info(cookies)
listH2=cookies.items()
for i in listH2:
    log.info(i)
log.info("********************cookies********************")

response.close()




if __name__ == "__main__":
    log.info("end")
#INFO:test:init
#INFO:test:<Response [419]>
#INFO:test:{'Date': 'Thu, 18 Apr 2024 07:53:15 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Cache-Control': 'no-cache, private', 'Set-Cookie': 'wallhaven_session=eyJpdiI6ImRXdU13R3ROYmJJdWZJRDdIWmp0XC93PT0iLCJ2YWx1ZSI6InRFWWNibXhJUEdqaENES2w2TDBPNzFtOGZUUnllc1RXc0U4TkgwYm9Xbk91aldEbDRpOG93UEZhaExlcGVaem0iLCJtYWMiOiJkN2IwNzNjYzNhMGM4YTc4MzQ1MTNjYzU4ZjcxZmRkMmYxYzZmNzE5NGRkMDUwZGM2ZWQ4ZWEyYTQwYTgxMDVmIn0%3D; expires=Thu, 18-Apr-2024 09:53:15 GMT; Max-Age=7200; path=/; secure; httponly; samesite=strict', 'X-Frame-Options': 'sameorigin', 'CF-Cache-Status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v4?s=6NgjnqU2a9kxe6r21pDjDArqwW7H6GSUomSJ9%2F9u9bImwnST%2BvQ49pClv%2Bmtb7yRevXa4FlH2Hl8Y9ofEAlRpGGWlfQh7gCtWW3c126pSSAQfG3v0ZL10gYx17BWzA%3D%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '8763147c0b01102d-LAX'}
#INFO:test:<RequestsCookieJar[<Cookie wallhaven_session=eyJpdiI6ImRXdU13R3ROYmJJdWZJRDdIWmp0XC93PT0iLCJ2YWx1ZSI6InRFWWNibXhJUEdqaENES2w2TDBPNzFtOGZUUnllc1RXc0U4TkgwYm9Xbk91aldEbDRpOG93UEZhaExlcGVaem0iLCJtYWMiOiJkN2IwNzNjYzNhMGM4YTc4MzQ1MTNjYzU4ZjcxZmRkMmYxYzZmNzE5NGRkMDUwZGM2ZWQ4ZWEyYTQwYTgxMDVmIn0%3D for wallhaven.cc/>]>
#INFO:test:end
