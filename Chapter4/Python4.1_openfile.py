import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("i")

with open('/mytxt.txt', 'r', encoding='utf-8') as f:
    line = 'start'
    try:
        while line:
            line = next(f, None)
            print(line, end='')
    except StopIteration:
        pass
if __name__ == "__main__":
    log.info("yy")