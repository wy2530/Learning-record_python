'''
六：json&pickle模块
    #1、什么是序列化
    序列化指的是把内存的数据类型转换成一个特定的格式的内容
    该格式的内容可用于存储或者传输给其他平台使用

    内存中的数据类型 ---->序列化 ---->特定的格式（json格式或者pickle格式）
    内存中的数据类型 <----序列化 <----特定的格式（json格式或者pickle格式）

    #2、为何要序列化
        （1）可用于存储===>可以用于存档(内存中的数据以某种形式存入硬盘)
            可以是专用格式：pickle只有python语言可以识别
            可以用json，但不推荐
        （2）传输给其他平台使用===>跨平台数据交互
            通用格式，能够被所有语言识别的格式==json
            json只是提取了所有语言共有的特点，但语言独有的特点不行
    #3、如何使用序列化与反序列化
        (1)
            json.dumps()
            json.loads()
        (2)
            json.dump()
            json.loads()
        (3)补充：
            json只是提取了所有语言共有的特点，但语言独有的特点不行，
             例如python中的集合，不可以序列化
        强调：json格式没有单引号格式
    #4、猴子补丁
        核心思想：对源码中有些地方不满意，用自己的代码来代替源代码中的某一部分功能
                可以在程序的启动文件中修改。不想要便可直接注释。注意：不可以直接修改源代码。
    #5、pickcle模块
        集合可以识别，但是读写文件应该是b模式
七：shelve模块
八: xml模块

九:configparser模块
    (遗留：settings的配置文件？？？)
    添加某种特定格式的配置文件
十 :hashlib模块
    1、什么是哈希
        hash是一类算法，该算法接受传入的内容，经过运算得到的一串 hash
        hash值的特点：
            （1） 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
            （2）不能由 hash值返解成内容=======》把密码做成 hash值，不应该在网络传输明文密码
            （3）只要使用的 hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的
    2、hash用途
     （1）密文
     （2）完整性校验
    3、如何用
     （1）撞库
     （2）加盐
十一:suprocess模块 ： 获取到命令执行结果的返回值
    子进程
十二：logging模块
    import logging
    logging.debug("XXX")
    logging.info("XXX")
    logging.warning("XXX")
    logging.error("XXX")
    logging.critical("XXX")
'''

# #3、如何使用序列化与反序列化
# #示范一：
# import json
# #json.dumps 转化为json格式
# json_res=json.dumps(True)
# print(json_res,type(json_res))
#
# json_res2=json.dumps([1,'aaa',True,False])
# print((json_res2,type(json_res2)))
#
# #json.loads 反序列化
# cover_json=json.loads(json_res)
# print(cover_json,type(cover_json))
#
# cover_json2=json.loads(json_res2)
# print(cover_json2,type(cover_json2))

#示范二
import json
#1)已json格式存入文件(json是字符串格式，可以使用t模式写入)
# json_res=json.dumps([1,'aaa',True,False])
# with open('text.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)
#2)将json格式已Py格式读出
# with open('text.json',mode='rt',encoding='utf-8') as f:
#     res=f.read()
#     print(json.loads(res))

#将序列化的结果写入文件的简单方法,dump可以一步到位
# with open('text.json',mode='wt',encoding='utf-8') as f:
#     json.dump([1,'aaa',True,False],f)
#将json格式已Py格式读出的简单办法
# with open('text.json',mode='rt',encoding='utf-8') as f:
#     res=json.load(f)
#     print(res)

# #json验证：
#import json
# res=json.dumps({1,2,3})
# print(res) #Object of type set is not JSON serializable

#中文验证
# res=json.dumps({'name':'我'})
# print(res,type(res))

# res=json.loads('{"name": "\u6211"}')
# print(res)


'''
#4)猴子补丁例子
ujson 模块 比json 模块要更快

import json
import ujson
def monkey_patch_json():
    json.__name__='ujson'
    json.dumps=ujson.dumps
    json.loads=ujson.loads
monkey_patch_json() #在文件入口处执行

#以下办法不可以，因为名称空间并没有改变
import ujson as json

'''

# #5)pickle模块:写
# import pickle
# res=pickle.dumps({1,2,3,4,5})
# # print(res,type(res))
# with open('text2.json',mode='wb') as f:
#     f.write()
# #5)读
# import pickle
# #res=pickle.dumps({1,2,3,4,5})
# # print(res,type(res))
# with open('text2.json',mode='rb') as f:
#     res=f.read()
#     print(pickle.loads(res))

# import configparser
# config=configparser.ConfigParser()
# config.read('test.ini')

# #1、获取sections
# print(config.sections())
#
# #2、获取某一section下的所有options
# print(config.options('section1'))
#
# #3、获取items(元组)
# print(config.items('section1'))
#
# #4、
# res=config.get('section1','user')
# print(res,type(res))
#
# #5、getint 将 str转化为int类型
# res1=config.getint('section1','age')
# print(res1,type(res1))
#
# #6、getboolean 将 str转化为bool类型
# res2=config.getboolean('section1','is_admin')
# print(res2,type(res2))


'''
3、如何用哈希
'''
# import hashlib
# #m相当于hash工厂
# m=hashlib.md5()
# #原料 bits类型
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# #合成
# res=m.hexdigest() #'helloworld'
# print(res)

#1)验证
# m1=hashlib.md5()
# m1.update('he'.encode('utf-8'))
# m1.update('llo'.encode('utf-8'))
# m1.update('world'.encode('utf-8'))
# res1=m1.hexdigest() #'helloworld'
# print(res1)

#2)校验完整性
'''
在文件校验时，一般若文件很大，则不会全部校验
只会选取一部分来进行校验
因此，可以f.read(2000),根据字节数来读取
但是只固定几个字节，可能不够随机
因此可以 使用f.feek() 移动指针位置随机获取字节
'''

'''
hash撞库，破坏者可能通过大量随机密码来破解
模拟撞库
'''
# import hashlib
# #m相当于hash工厂
# m=hashlib.md5()
# #原料 bits类型
# m.update('wy'.encode('utf-8'))
# m.update('453521'.encode('utf-8'))
# #合成
# res=m.hexdigest() #'helloworld'
# print(res)

# cryptograph='fc5e038d38a57032085441e7fe7010b0'
# passwds=[
#     'wy123..',
#     'wy990619',
#     'wy990731',
#     'woaini...',
#     'wy1234',
#     '453421',
#     'wy8888',
#     'helloworld',
# ]
# import hashlib
# dic={}
# for p in passwds:
#     res=hashlib.md5(p.encode('utf-8'))
#     dic[p]=res.hexdigest()
# # print(dic)
# for k,v in dic.items():
#     if v==cryptograph:
#         print("明文密码为：%s"%k)
#         break
# else:
#     print("撞库失败")

#提升撞库成本==>密码加盐"加干扰"
# import hashlib
# m=hashlib.sha3_512()
# m.update('hello'.encode('utf-8'))
# m.update('哈哈'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res=m.hexdigest()
# print(res)


# import subprocess
# obj=subprocess.Popen('ls/root',shell=True,
#                  stdout=subprocess.PIPE,#正确结果
#                  stderr=subprocess.PIPE,#错误解决
#                  )
# print(obj)
# err_res=obj.stderr.read()
# print(err_res) #读出来的是二进制类型，需要解码
# #解码的编码：编码应该用系统的编码,因为运行的是系统程序
# print(err_res.decode("gbk"))

