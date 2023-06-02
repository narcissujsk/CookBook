import time
from functools import wraps


def timethis(func):
    @wraps(func)#保存函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        print("this is a wrapper")
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1
        time.sleep(0.01)


# 装饰器就是一个函数,接受一个函数,并返回一个新的函数作为输出
# @timethis
# def countdown(n):
#
# 效果等同于
# def countdown(n):
# countdown=timethis(countdown)
#
if __name__ == "__main__":
    print('')
    countdown(111)
