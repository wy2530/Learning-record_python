from multiprocessing import Process
from threading import Thread

import time


def task(name):
    print("%s is running" % name)
    time.sleep(1)
    print('%s is over' % name)

'''
开启线程不需要再main下面执行，直接书写即可
但是我们还是习惯性的将启动命令写在main下面
'''
if __name__ == '__main__':
    t = Thread(target=task,args=('hello',))
    t.start()
    # p= Process(target=task,args=('AAA',))
    # p.start()
    print("主进程")

'''
你可能会发现线程比进程快，因为进程申请需要开辟内存空间，需要时间
而线程不需要时间
'''