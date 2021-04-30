from multiprocessing import Process
import time


class MyProcess(Process):
    def run(self):  # 函数名必须叫run
        print("hello is run")
        time.sleep(3)
        print("over")


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('开始了')
