# from multiprocessing import Process, Queue
#
#
# def task1(q):
#     print("我是子进程1")
#     q.put(111)  # 3、我把一个东西放入了队列
#
#
# if __name__ == '__main__':
#     q = Queue()  # 1、创建一个队列
#     p = Process(target=task1, args=(q,))
#     p.start()  # 2、开始了一个进程
#     p.join()  # 这里这一步并不需要，因为get()如果没有东西会阻塞，直到有东西
#     print(q.get())  # 4、我从子进程中将队列中的东西取出来了

from multiprocessing import Process, Queue
import time

def task1(q):
    q.put("我是第一个进程放进去的")  # 3、我把一个东西放入了队列


def task2(q):
    q.put("我是第二个进程放进去的")
    time.sleep(0.3)
    print("我是第二个进程取出来的：", q.get())

'''
有个小问题：队列，先进先出啊，不应该先取进去的那一个吗
'''

def task3(q):
    print("我是第三个进程取出来的：", q.get())


if __name__ == '__main__':
    q = Queue()  # 1、创建一个队列
    p1 = Process(target=task1, args=(q,))
    p2 = Process(target=task2, args=(q,))
    p3 = Process(target=task3, args=(q,))
    p1.start()  # 2、开启了一个子进程
    p2.start()  # 3、开启了另一个子进程
    p3.start()