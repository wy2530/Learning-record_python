from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    # print("hehhe")
    time.sleep(3)
    print('%s is over' % name)


if __name__ == '__main__':
    # 1、创建一个对象  Process是一个类
    '''
    补充一个小技巧： ('hello',)
        容器类型的，哪怕只有一个元素，也要有逗号隔开
        尤其是元组类型，不加，会有问题的
    '''
    p=Process(target=task,args=('hello',))  # 目标进程和参数
    # 2、开始进程
    p.start()  # 告诉操作系统来帮你创建一个进程
    '''
    执行结果为：
        开始了...
        hello is running
        hello is over
    
    也就是说：发起开始进程的指令之后，并没有等着那个指令执行完再去执行其他的
            属于异步操作
    '''
    # time.sleep(3)
    # p.join()  # 为了让子进程p先执行，加sleep会控制不好时间
    print('开始了...')
    print("主进程")



'''
一个文件，点击运行时就是开启了一个进程

那么如何再进程里在开启一个进程呢？
首先要知道的知识点：
    1、在windows操作系统下创建进程，类似于模块导入的方式，也就是会从头到尾的去执行某个文件
    2、在linux中则是直接将代码完整的拷贝一份

举个例子：
XXX:表示我写的代码


    XXXXXX
    XXXXXX
    XXXXXX
    
    创建进程1:XXX   #当程序从上到下执行到进程1时，又需要以模块导入的方式从上到下执行一遍，会陷入死循环，程序报错
    创建进程2:XXX
    
那么解决方案：使用main
    关于 if  __name__ == '__main__' 的一点解释：
        当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行
        当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行

重点记一句话：
    也就是说，为了避免程序陷入死循环，在windows操作系统下，创建进程一定要在main内创建
'''
