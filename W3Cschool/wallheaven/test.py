import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")

from Image import Image

url = 'https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png'


image = "wallhaven-6do9zx.png"
dir = "D:/wallheaven/test/";
a=Image(image,url,dir)
a.download()
if __name__ == "__main__":
    log.info("end")
