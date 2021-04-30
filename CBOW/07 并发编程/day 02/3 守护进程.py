from multiprocessing import Process
import time


def task():
    print("进程1正在活着")
    time.sleep(3)
    print("进程1正在死亡")


if __name__ == '__main__':
    p = Process(target=task)
    p.daemon = True  # 将进程p设置为守护进程（不可以在子进程开始之后设置，会报错）
    p.start()
    # time.sleep(4)
    print("主进程死亡")


'''
主进程死亡时：守护进程也不可以存活

设置完daemon之后，你会发现，子进程都没有运行（因为主进程已经死了）
'''