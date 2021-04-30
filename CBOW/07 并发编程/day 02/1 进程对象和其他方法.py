from multiprocessing import Process, current_process
import time
import os


def task():
    # print("%s is running" % current_process().pid)  # 查看当前进程的pid号
    print("%s is running" % os.getpid())  # 查看当前进程的pid号
    print("%s子进程父进程" % os.getppid())  # 查看当前进程的pid号
    # time.sleep(30)  # 要有延时才可以查到，不然一运行就结束了...


if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.terminate() # 杀死当前进程
    time.sleep(0.1)
    print(p.is_alive())  # 如果刚刚杀死就判断，可能结果为True,因为操作系统去执行那个命令需要时间，但代码运行速度有非常快
    print("主进程",current_process().pid)
    print("主进程父进程" ,os.getppid())  # 查看当前进程的父pid号

