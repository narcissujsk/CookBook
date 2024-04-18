import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

if __name__ == "__main__":
    log.info("end")
