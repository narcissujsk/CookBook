import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

#daemon线程无法被连接,主线进程结束后会自动销毁
#A boolean value indicating whether this thread is a daemon thread (True) or not (False).
# This must be set before start() is called, otherwise RuntimeError is raised.
# Its initial value is inherited from the creating thread;
# the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False
#The entire Python program exits when no alive non-daemon threads are left.
# 这个属性为一个布尔值，表示是否为一个守护进程，且这个属性设置必须在线程的start方法开始之前调用。
# 它的值继承自主线程，主线程的daemon为False且所有从主线程创建的线程都是daemon = False的。
# 下面一句说明了，python主程序只有在没有非守护线程的时候才会退出
t = Thread(target=countdown, args=(10,))
#t = Thread(target=countdown, args=(10,),daemon=True)
#默认情况下 主线程中创建的daemon=False,不会阻塞主线程的执行,主线程执行完之后,如果子线程还没执行完,子线程会继续执行完
#当子线程执行完成之后,程序才退出
# 如果子线程是daemon线程,主线程执行完之后,子线程会自动销毁

if __name__ == "__main__":
    t.start()
    time.sleep(1)
    print(t.daemon)
    print( "d")

