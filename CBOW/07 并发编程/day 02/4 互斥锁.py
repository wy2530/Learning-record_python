from multiprocessing import Process,Lock
import json
import time
import random


# 模拟火车票

# 查票
def search(i):
    with open("data.json", 'r', encoding="utf-8") as f:
        dic = json.load(f)
    print("用户%s查询余票，还剩%s张票" % (i, dic.get('ticket_num')))


'''
小知识:
    在使用字典取值的时候，最好不要使用[]的方式，应该使用dic.get("key")的方式
    原因：
        dic["key"]:在key不存在时，会报错
        dic.get("key"):在key不存在时，不报错，返回None
'''


# 买票 （两步：1、查票 2、买票）

def buy(i):
    with open("data.json", 'r', encoding="utf-8") as f:
        dic = json.load(f)

    # 可能会有网络延时 （模拟网络延时）
    time.sleep(random.randint(1, 3))

    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        # 写入
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print("用户%s购票成功" % i)
    else:
        print("用户%s购票失败"% i)


# 任务整合

def run(i, mutex):
    search(i)
    # 给买票环节加锁处理 (随机的)
    # 抢锁
    mutex.acquire()
    buy(i)
    # 释放锁
    mutex.release()


# 现在模拟大家同时买票，也就是多线程

if __name__ == '__main__':
    # 不可让所有用户同时买票，因此加一把锁
    # 在主进程中生成一把锁，让所有子进程抢
    mutex = Lock()

    for i in range(1,11):
        p = Process(target=run,args=(i,mutex))
        p.start()


'''
运行结果：你会发现，只剩一张了，但是大家都买到了票

如果加了锁：你会发现只有一个人抢到了，谁抢到是随机的
'''