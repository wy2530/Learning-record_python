from multiprocessing import Process
import time


def task(name,n):
    print('%s is running' % name)
    # print("hehhe")
    time.sleep(n)
    print('%s is over' % name)


if __name__ == '__main__':

    # 异步的
    # p1 = Process(target=task, args=('hello',1))  # 目标进程和参数
    # p2 = Process(target=task, args=('world',2))  # 目标进程和参数
    # p3 = Process(target=task, args=('nihao',3))  # 目标进程和参数
    #
    # start = time.time()
    # p1.start()  # 告诉操作系统来帮你创建一个进程
    # p2.start()  # 告诉操作系统来帮你创建一个进程
    # p3.start()  # 告诉操作系统来帮你创建一个进程


    '''
    结论：
    1、每一次运行的结果不一定相同，因为进程的时候并不确定不知道谁快谁慢
    2、多个进程之间是独立的，可以同时进行，因此时间不是单纯的相加
    3、都是异步的
    '''
    # p1.join()
    # p2.join()
    # p3.join()
    #

    start = time.time()
    p_list = []
    for i in range (1,4):
        p=Process(target=task,args=('子进程%s' %i, i))
        p.start()
        # p.join() # 如果把join写在这里，就变成了串行了
        p_list.append(p)
    for p in p_list:
        p.join()
    print('开始了...')
    print("主进程 %s" %(time.time()-start))
