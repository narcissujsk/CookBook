import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")


if __name__ == "__main__":
    src = 'https://wallhaven.cc/w/28mkg9'
    fullUrl='https://w.wallhaven.cc/full/28/wallhaven-28mkg9.jpg'
    # print(src)
    # pic_name = src[-6:]
    # print(pic_name)
    # print(pic_name[:2])
    # fullUrl = 'https://w.wallhaven.cc/full/'+pic_name[:2]+'pic_name[:2]'
    pic_name = fullUrl[-20:]
    print(pic_name)
    log.info("end")
