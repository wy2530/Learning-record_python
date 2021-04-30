from threading import Thread
import time


class MyThread(Thread):
    """
    针对双下划线结尾的方法，统一读成 双下init
    """
    def __init__(self):
        # 重写了别人的方法
        pass


    def run(self):  # 函数名必须叫run
        print("hello is run")
        time.sleep(3)
        print("over")


if __name__ == '__main__':
    p = MyThread()
    p.start()
    print('开始了')
