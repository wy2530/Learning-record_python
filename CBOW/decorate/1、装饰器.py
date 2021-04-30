"""
1、*args **kwargs
2、名称空间与作用域：名称空间的 “嵌套”关系是在函数定义阶段，检测语法的时候确认的
3、函数对象：
  可以把函数当做参数传入
  可以把函数当做返回值（不要加括号！！！！）
4、函数的嵌套定义：
    函数内写函数
5、闭包函数
  函数里面的函数变量，是上一层函数里的
  最后再外层函数中返回里面的函数

  传参的方式：
    一、通过参数传递
    二、通过闭包函数传递



什么是装饰器:
    工具（函数、类）添加额外的功能
为何要用装饰器：再不改变源代码和调用方式的情况下，增加扩展功能
   开放封闭原则
    开放：指的是对扩展功能是开放的
    封闭：指的是对修改源代码是封闭的
如何
"""

'''
要求：添加一个功能：统计运行时间
'''

# import time
#
# def timmer(func):
#     # func=原来wapper的内存地址
#     def wapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)  # 目的：将函数返回值写活
#         end = time.time()
#         print(end - start)
#         return res
#
#     return wapper  # 返回wapper的原因是让他重新变成全局变量调用
#
#
# @timmer  # index=outter(index)
# def index(x, y):
#     time.sleep(3)
#     print(x, y)
#     return 123


'''
将参数写活了之后，wapper是一个封装的功能，但是目前只能给index使用
'''

# def wapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     end = time.time()
#     print(end-start)
#
#
# wapper(111,222)


# index=outter(index) #原来wapper的内存地址

'''
不方便的地方是你每一次写都需要把被装饰的函数写在outter里面，
有个简单的办法：在被装饰的函数前面写上@装饰器名 即可
'''

# res = index(111, 222)  # 相当于在调用wapper
#
# print(res)

'''
思考题：
    如果一个函数有多个装饰器怎么运行，运行过程是怎样的？
答案：先运行最下方的装饰器

@deco1   #index=deco1(deco2.wrapper的内存地址)
@deco2   #deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
@deco3   #deco3.wrapper的内存地址=deco3(index)
def index():
    pass
'''

'''
装饰器作用：
    1、调用原函数
    2、补充新功能
'''
# 无参装饰器模板
# def outter(func):
#     def wapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wapper


'''
@语法的作用：
 @outter  #相当于index=outter(index) 
如果我写成@print("hello")
    执行步骤：
    1、先执行这个函数
    2、将函数的转为@后的东西
    3、但不一定可以运行
@None 
'''
# @print
# def home(a,b,c):
#     pass
#
# print(home)  # None 因为home没有返回值

'''
装饰器的补充：

    print(index.__name__)  #可以查看函数的名字，加装饰器后名字是wapper,不加装饰器名字是index
    # print(help(index)) 
    print(index.__doc__)  #help()可以查看原函数中的注释，查看的是原函数__doc__属性下的注释
    
    为了使wapper()和index()函数更像，需要将属性也替换掉，但是属性过多，每行都写不现实，
    因此python提供了简单的办法，可以导入模块来装饰wapper()的属性
    
from functools import wraps #导入模块

@wraps(func) #在需要 被装饰的 装饰器函数 正上方写（需要传参，参数为需要改变的函数对象）
'''
# import time
# from functools import wraps
#
# def timmer(func):
#     # func=原来wapper的内存地址
#     @wraps(func)
#     def wapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)  # 目的：将函数返回值写活
#         end = time.time()
#         print(end - start)
#         return res
#
#     return wapper  # 返回wapper的原因是让他重新变成全局变量调用
#
#
# @timmer  # index=outter(index)
# def index(x, y):
#     time.sleep(3)
#     print(x, y)
#     return 123

'''
补充：
    由于语法糖@的限制，outter函数只能有一个参数，就是正下方的函数。不能有多个参数   -----相当于这一行 # index=outter(index)
    
那么我们现在知道了,wapper()中的参数不能改，outter函数中的参数也不能改，那怎么做需要传参的装饰器呢

解决还需要参数的情况：再套一层
'''

# 例如：写一个认证功能的装饰器，账户密码可来自文件，可来自数据库，可来自其他软件


'''
现在的问题是闭包函数内的db_type也需要一个参数
    在补充知识是写到，第一层参数不可修改，外一层参数也不可修改，那么只能再通过一次闭包来进行传递了
'''


def auth(db_type):
    # db_type=111
    def deco(func):
        def wapper(*args, **kwargs):
            user = input("输入名字：")
            pwd = input("输入密码：")

            if db_type == 'file':
                print("基于文件的输入")
                res = func(*args, **kwargs)
                return res

            elif db_type == 'mysql':
                print("基于mysql的输入")
                res = func(*args, **kwargs)
                return res
            elif db_type == 'other':
                print("基于mysql的输入")
                res = func(*args, **kwargs)
                return res
            else:
                print("不可认证")

        return wapper

    return deco


'''
如何使用这层闭包：auth(deco)

# deco = auth(db_type='file')
# @deco

@auth(db_type='file')

上面俩行与下面的一行用法相同，先执行@之后的语句，在使用@

注意：没必要闭包四层，因为第三次已经是可以传各种参数了
'''


# deco = auth(db_type='file')
# @deco
@auth(db_type='file')
def index(x, y):
    print(x, y)


deco = auth(db_type='mysql')


@auth(db_type='mysql')
def home(x, y):
    print(x, y)


home(1, 2)
