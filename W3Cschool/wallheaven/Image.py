import threading

import requests
import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        # 如果目录不存在，则创建它
        os.makedirs(directory_path)
        log.info(f"目录 '{directory_path}' 已创建！")


class Image:
    url = "";

    def __init__(self, url):
        self.url = url

    def download(self):
        try:
            log.info(threading.current_thread().getName() + " "+"try to download image"+self.url)
            # 发送请求并获取图片数据
            # fullUrl='https://w.wallhaven.cc/full/28/wallhaven-28mkg9.jpg'
            name = self.url[-20:]
            path2 = self.url[28:30]
            path2 = "test"
            directory_path = "D:/wallheaven/full/" + path2 + "/";
            create_directory(directory_path)
            response = requests.get(self.url)
            path = directory_path + name;
            #log.info(threading.current_thread().name+" "+path)
            # 将图片数据写入本地文件
            if os.path.exists(path):
                log.info(threading.current_thread().name+" "+path+" 文件存在")
            else:
                with open(path, 'wb') as file:
                    file.write(response.content)
                log.info(threading.current_thread().name + " " + self.url + "  downloaded")
        except Exception as e:
            log.error(e)

        return
