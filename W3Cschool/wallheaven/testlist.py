import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")
import requests
from bs4 import BeautifulSoup
from lxml import etree
url = "https://wallhaven.cc/search?categories=111&purity=111&sorting=date_added&order=desc&ai_art_filter=1&page=2"

payload = {}
files={}
headers = {
    'Authorization': 'Basic MTc5MTEyMTA5NEBxcS5jb206Mzg1MTUyanNr',
    'Cookie': 'XSRF-TOKEN=eyJpdiI6Img0SXVTXC9ubGRqdll0TnFPT0U5VXJnPT0iLCJ2YWx1ZSI6IjRpcVpzOVo0RUdFZWl1VGMraURVdHVkQzhoNGRvaHgzejlOQUkwTzJhZXpLUFBVSmRQeitVTkNvOG5SNEpVVkUiLCJtYWMiOiI1NzhlZThkMDdhNThlM2ZjM2ExNmQ0MTllMGI3OWFkMjBiYWU5OGY2ODhkMWNhZjhmMjNkZTE1NTg0MDgzYWYzIn0%3D; wallhaven_session=eyJpdiI6InRrTW9tVTVoN3ROcjhCbGZVM0JLZUE9PSIsInZhbHVlIjoienlOOXc3N21EbjRQWlVqekdrblwvbEpQXC9RQXdtM2hJUmhwSFBcL2FhVzZkSDNyVE1kQmVIK0FROWNqbjFiR2FZRSIsIm1hYyI6IjFhODJjODAxNGE4NWU2YTYyNDFlNGEyNDA0M2ZjODQ3NWE1NjI3ZmYxOWZhYWEwNjU2OTdjNjY0OGNiOWMwNmQifQ%3D%3D'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)
soup = BeautifulSoup(response.content,'lxml')
print(soup.title)

print(soup.select(".lazyload"))

if __name__ == "__main__":
    log.info("end")
