import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")

import os

def create_directory(directory_path):
    """
    自动检查并创建文件目录。

    参数:
        directory_path (str): 目标目录的路径。

    返回:
        None
    """
    # 检查目录是否存在
    if not os.path.exists(directory_path):
        # 如果目录不存在，则创建它
        os.makedirs(directory_path)
        print(f"目录 '{directory_path}' 已创建！")
    else:
        print(f"目录 '{directory_path}' 已存在。")

# 使用示例


if __name__ == "__main__":
    create_directory("D:/wallheaven/full/6d/")
    log.info("end")
