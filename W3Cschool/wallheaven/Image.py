import threading
import logging
import logging.config
from logging import config

import requests
import logging
import os

logging.config.fileConfig('./logging.conf')
# 创建 logger
logger = logging.getLogger('root')


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        # 如果目录不存在，则创建它
        os.makedirs(directory_path)
        logger.info(f"目录 '{directory_path}' 已创建！")


class Image:
    url = "";
    num = 0

    def __init__(self, url):
        self.url = url

    def __init__(self, url,num):
        self.url = url
        self.num = num

    def download(self):
        try:
            logger.info(threading.current_thread().getName() + " "+"try to download image "+self.url)
            # 发送请求并获取图片数据
            # fullUrl='https://w.wallhaven.cc/full/28/wallhaven-28mkg9.jpg'
            name = self.url[-20:]
            directory_path = "D:/wallheaven/full/" + str(self.num) + "/";
            directory_path = "D:/wallheaven/full/test/";
            logger.info("name is "+name +" num is "+str(self.num))
            create_directory(directory_path)
            response = requests.get(self.url)
            path = directory_path + name;
            #log.info(threading.current_thread().name+" "+path)
            # 将图片数据写入本地文件
            if os.path.exists(path):
                logger.info(threading.current_thread().name+" "+path+" 文件存在")
            else:
                with open(path, 'wb') as file:
                    file.write(response.content)
                logger.info(threading.current_thread().name + " " + self.url + "  downloaded")
        except Exception as e:
            logger.error(e)

        return
