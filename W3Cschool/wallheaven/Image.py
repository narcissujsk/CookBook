import requests
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')


class Image:
    image = "";
    url = "";
    dir = "";


    def __init__(self, image, url, dir):
        self.image = image
        self.url = url
        self.dir = dir

    def download(self):
        # 发送请求并获取图片数据
        response = requests.get(self.url)
        path = self.dir + self.image;
        # 将图片数据写入本地文件
        with open(path, 'wb') as file:
            file.write(response.content)
        log.info(self.url+"  downloaded")
