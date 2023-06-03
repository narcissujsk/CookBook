

import math
from functools import partial


def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)


points=[(1,2),(3,4),(5,6),(7,8)]

# print(distance((0,0),(3,4)))
# pt=(0,0)
# points.sort(key=partial(distance,pt),reverse=True)#降序排列
# print(points)


def add(x,y):
    return x+y


def output_result(result,log=None):
    if log is not None:
        log.debug('got:%r',result)


# if  __name__=="__name__":
if __name__ == "__main__":
    print("Start Running")
    import  logging
    from functools import partial
    from multiprocessing import Pool

    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger('test')
    p=Pool()
    p.apply_async(add,(3,4),callback=partial(output_result,log=log))
    p.close()
    p.join()
