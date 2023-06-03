import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


t = Thread(target=countdown, args=(10,))

if __name__ == "__main__":
    t.start()
    t.join()
    print( "d")

