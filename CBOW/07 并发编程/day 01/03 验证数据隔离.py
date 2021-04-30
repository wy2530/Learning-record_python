from multiprocessing import Process

money = 100  # 全局变量是100


def task(name):
    global money
    money = 666  # 修改了全局变量
    print("%s is running..." % name)
    print("子进程中的%s" % money)


if __name__ == '__main__':
    '''
    target后面是函数名字，不是字符串，不要弄错了！！！
    '''
    p = Process(target=task, args=("hello",))
    p.start()
    p.join()
    print("主进程中的%s" % money)
