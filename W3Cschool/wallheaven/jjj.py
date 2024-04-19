import os
import threading

import requests
from lxml import etree

"""
爬取网站：https://wallhaven.cc/
"""
# 伪装浏览器请求
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# 存放下载图片的文件夹名称
new_folder = 'img'
# 5个模块对应的字符串列表
type_list = ['hot', 'toplist', 'latest', 'random']
# 线程池
threads = []

# 单页下载，只下载一页24张图片
def get_wall_one_page(type_index: int, page_num) -> None:
    # page_num爬取的页码
    url = 'https://wallhaven.cc/{}?page={}'.format(type_list[type_index], page_num)
    print(url)
    # 获取当前目录
    current_dir = os.getcwd()

    # 新文件夹的名称
    # new_folder = 'img_{}'.format(type_list[type_index])  # 创建新文件夹
    if not os.path.exists(new_folder):
        os.mkdir(os.path.join(current_dir, new_folder))

    res = requests.get(url, headers=headers).text
    selector = etree.HTML(res)
    img_urls = selector.xpath('//a[@class=\'preview\']/@href')
    detail_img(img_urls)

def detail_img(img_urls):
    """
    图片详情
    :param img_urls:获取到单个图片item的详情url
    :return:
    """
    i = 0

    for item in img_urls:
        son_res = requests.get(item, headers=headers).text
        selector = etree.HTML(son_res)
        src_arr = selector.xpath('//img[@id=\'wallpaper\']/@src')
        # 使用多线程下载图片
        t = threading.Thread(target=download_img, args=(src_arr[0], i))
        t.start()
        threads.append(t)
        # download_img(src_arr[0], i)

        i += 1
        # 等待所有线程完成
    for t in threads:
        t.join()
    print("当前页所有图片下载完成")

def download_img(img_src, i):
    """
    图片下载
    :param img_src: 图片的src
    :param i: 序号
    :return: void
    """
    with open('./{}/{}-{}'.format(new_folder, i, img_src.split('/')[-1]), 'wb') as f:
        f.write(requests.get(img_src).content)
    print(i, img_src)

def get_num(type_index):
    """ 获取总页码
    :param type_index:爬取的类型索引
    :return:当前的页码数量
    """
    url = 'https://wallhaven.cc/{}?page=2'.format(type_list[type_index])
    selector = etree.HTML(requests.get(url, headers=headers).text)
    page_num = selector.xpath('//header[@class=\'thumb-listing-page-header\']/h2//text()')
    return ''.join(page_num).split(' ')[-1]

def get_total(type_index, start, end):
    """
    爬取指定类型，页码范围
    :param type_index:
    :param start:
    :param end:
    :return:
    """
    # total = int(get_num(type_index))
    if end is None:
        end = total
    if start is None:
        start = 1
    try:
        for i in range(start, end):
            url = 'https://wallhaven.cc/{}?page={}'.format(type_list[type_index], i)
            print(url, '开始下载第{}/{}页'.format(i, end - 1))
            res = requests.get(url, headers=headers).text
            selector = etree.HTML(res)
            img_urls = selector.xpath('//a[@class=\'preview\']/@href')
            detail_img(img_urls)
            # threading.Thread(target=detail_img, args=(img_urls)).start()
    except Exception as e:
        print(e)

# https://wallhaven.cc/search?q=code&page=1
# todo 根据输入关键词，查找下载

if __name__ == '__main__':
    """
    0:'hot', 热榜
    1:'toplist', top排名
    2:'latest', 最新
    3:'random' 随机
    4:'search' 关键字查找
    """
    get_wall_one_page(1,1)  # 爬取单页
    # get_total(2, 1, 11)  # 爬取多个指定页码


