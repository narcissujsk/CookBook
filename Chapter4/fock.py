import logging,os,time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')

if __name__ == "__main__":
    log.info("yy")
    while True:
        time.sleep(3)
        os.fork()
        log.info(os.getpid())