# add中的内容是：abc你好abc你好
# 1)r+读取abc和好ab
# with open("add", mode="r+", encoding="utf-8") as f:
#     # seek读的是字节个数，一个汉字在utf-8编码中占3个字节
#     f.seek(6, 0)
#     # #read读的是字符个数，字符个数！
#     res = f.read(3)
#     print(res)  # 好ab
# # 2)字符替换
# with open("add", mode="r+", encoding="utf-8") as f:
#     f.seek(6, 0)
#     f.write("gjkhas")  # 会替换原来的字节
# # 3)w+模式：可读可写，每一次打开都会清空文件，读不出来
# with open("add", mode="w+", encoding="utf-8") as f:
#     res = f.read()
#     print(res)  # 会将add清空
# 4)a+模式：可读可写，追加模式，每次都在文件末尾，指针移动没用


# 3)、tail -f access.log程序实现
# tail -f access.log的意思是：监听access.log文件末尾是否有追加的内容

import time

with open("add", mode='rb') as f:
    # 指针移入文件末尾
    f.seek(0, 2)
    while True:
        line = f.readline()  # 读取一行
        if line:
            # b格式以UTF-8解码容易看明白,end=''是取消换行符的空格
            print(line.decode("utf-8"), end='')
        else:
            # 没有添加时，等待监听,可以模拟延时操作
            time.sleep(0.2)  # 每隔0.2秒监听一次

# #4)、证明一下覆盖
# with open('two',mode='rt+',encoding='utf-8') as f:
#     #文件指针指向第三个字节
#     f.seek(3,0)
#     #6个汉字会占用18个字符
#     f.write("修改文件内容")

# 5）修改文件:要求将文件中的hello替换成hi
# 错误方式：
# with open("add",mode='rt',encoding='utf-8') as f1,\
#     open("add",mode='wt',encoding='utf-8') as f2:
#     res=f1.read().replace('hello','hi')
#     f2.write(res)

# 正确方式一：
# with open("add",mode='rt',encoding='utf-8') as f1:
#     res=f1.read().replace('hi','hello')
# with open("add", mode='wt', encoding='utf-8') as f2:
#     f2.write(res)

# 正确方式二：
# 首先来看一下连续写入文件会不会清空文件
# with open('add',mode='wt',encoding='utf-8') as f:
#     f.write("sjagkd\n")
#     f.write("hfgihlk\n")

# import os
# #1.打开add文件     # 2.写入.add.swap文件
# with open('add', mode='rt', encoding='utf-8') as f1,\
#     open('.add.swap',mode='wt',encoding='utf-8') as f2:
#     #3.从f中按行读取文件
#     for line in f1:
#         #4.替换
#         res=line.replace('hello','hi')
#         f2.write(res)
# #以上文件创建了两个文本文件
# #1.删除原来的文件
# os.remove('add')
# #2.将新写入的文件名字替换为原来的文件
# os.rename('.add.swap','add')


# #1)、函数定义
# def 函数名(参数1，参数2...):
#     """文档描述"""
#     函数体
#     return 返回值

# def first_code():
#     two_code()
#     print("hahahha")
# def two_code():
#     print("后面执行的")
# first_code()
# def first_code():
#     pass

# with open("two",mode="wt",encoding="utf-8") as f:
#     f.writelines("hi hi hi\nhello hi hello\nhi hello hi")

# #1)函数修改文件方法一：
# def alter_file(old_src,str1,str2):
#     with open("{}".format(old_src),mode='rt',encoding='utf-8') as f:
#         res=f.read().replace("{}".format(str1),"{}".format(str2))
#     with open("{}".format(old_src),mode='wt',encoding='utf-8') as f2:
#         f2.write(res)
# alter_file("two","hi","hello")
#
#
# #2)函数修改文件方法二：
# import os
# def alter_file(old_src,str1,str2):
#     with open(r"{}".format(old_src),mode='rt',encoding='utf-8') as f,\
#         open(r"new_src",mode='wt',encoding='utf-8') as f2:
#         for line in f:
#             res=line.replace("{}".format(str1),"{}".format(str2))
#             f2.write(res)
#     os.remove("{}".format(old_src))
#     os.rename("new_src","{}".format(old_src))
# alter_file("two",'hello','hi')

# #3)函数:追加日志
# import time
# def tail(tail_file):
#     with open("{}".format(tail_file),mode="rt+",encoding='utf-8') as f:
#         f.seek(0,2)
#         while True:
#             line=f.readline()
#             if line:
#                 print(line,end='')
#                 continue
#             else:
#                 time.sleep(0.2)
# tail("add")

# #4)函数编写登录功能
# def login():
#     username=input("your name:").strip()
#     password=input("your password:").strip()
#     with open('two',mode='rt',encoding='utf-8') as f:
#         for line in f:
#             '''strip()是为了去除文本本身的换行符,属于空白字符'''
#             name,pwd=line.strip().split(":")
#             if name==username and password==pwd:
#                 print("login in successful")
#                 break
#             '''else是匹配给for的'''
#         else:
#             print("error")
# login()


# 5)函数编写注册功能
'''
1.判断用户名是否存在
2.密码输入两次，两次相同
3.存入文件
4、输出注册结果
'''

# def set_name():
#     username = input("your name:").strip()
#     with open("two",mode="rt",encoding="utf-8") as f:
#         for line in f:
#             name=line.split(":")[0]
#             # 循环遍历每一行，判断是否有重名
#             if name==username:
#                 print("用户名已存在，请重新输入")
#                 set_name()
#                 break
#         else:
#             while True:
#                 password = input("your password:").strip()
#                 password_again = input("your password again:").strip()
#                 with open("two", mode='at+', encoding='utf-8') as f:
#                     if password == password_again:
#                         '''用户名+密码写入文件'''
#                         f.write("\n{}:{}".format(username,password))
#                         print("注册成功")
#                         break
#                     else:
#                         print("密码不相同，请重新输入")
# set_name()


# ATM

# #1)示例一：默认参数的值是在函数定义阶段被赋值的
# m=2
# def func(x,y=m):  #注意：存入的是2的内存地址,不可变类型
#     print(x,y)
# m=2343
# func(1)  #1 2
#
# #2)示例二：
# m=[1111,]
# def func(x,y=m): #注意：存入的是m的内存地址，可变类型
#     print(x,y)
# m.append(3333333)
# func(1)  #1 [1111,3333333]
#
# #3)一般都用不可变类型

# def func(x,y,*z):
#     print(x,y,z)
#     print(type(z))
# func(1,2,3,4,5,67)


# #变长参数应用实例：
# #求和：事先不知道参数
# def my_sum(*x):
#     res=0
#     for item in x:
#         res+=item
#     return res
# sum=my_sum(1,2,2,7,10)
# print(sum)

# def func(x,y,**kwargs):
#     print(x,y,kwargs)
# func(1,y=2,g=3,z=10,H="wee")

# def func(x,y,**args):
#     print(x,y,args)
# func(1,y=2,z=6,h=8)  #多余的形参可以变成字典的形式
# func(1,y=2,z=[1,2,3]) #多余的形参可以变成字典的形式
# func(2,3,**{'k':1,'h':40,'z':40}) #多余的形参可以可以通过**打散变成字典的格式
# # func(2,3,{'k':1,'h':40,'z':40}) #不打散的情况下是会报错的，因为不是key=value的格式
#
# def func(x,y,z):
#     print(x,y,z)
# func(**{'x':1,'y':2,'z':9})  #通过**会还原成x=1,y=2,z=9的形式
# #func(**{'a':1,'h':2,'z':9}) #通过**打散后,a,h,z与x,y,z并不对应，会报错
# func(*{'x':1,'y':2,'z':9})   #通过*打散的只能将key赋值给变量
# func(*{'a':1,'h':2,'z':9})   #赋值情况为x='a',y='h',z='z'

# def func(x,y,**kwargs):
#     print(x,y,kwargs)
# func(**{'y':222,'x':111,'a':333,'b':444})

"""
分开来看
1）先打散func中的实参：
    func(y=222,x=111,a=333,b=444)
2) 对应函数形参：
    很明显x=111,y=222, a和b是溢出的，保存为字典类型
"""

# #规定*args在**kwargs前面，不然会报错
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,4,x=1,y=2,c=3)
# print("=======")
# func(1,2,3,{'k':1,'h':2},j=3)

# def count(str):
#     num = 0
#     letter = 0
#     space = 0
#     other = 0
#     for x in str:
#         if x>='0' and x<'9':
#             num=num+1
#         elif (x>='a' and x<='z') or (x>='A' and x<='Z'):
#             letter=letter+1
#         elif x==' ':
#             space=space+1
#         else:
#             other=other+1
#     print(num,letter,space,other)
# count("12345 &*%$ ABCabc")


'''1、函数，判断字符串中字母、数字、空格、其他的个数'''
# def count(str):
#     dic={
#         'num':0,
#         'letter': 0,
#         'space':0,
#         'other': 0
#     }
#     #1)遍历字符串
#     for line in str:
#         #2)判断是否是数字
#         if line.isdigit():
#             dic['num']+=1
#         #3)判断是否是字母
#         elif line.isalpha():
#             dic['letter']+=1
#         #4)判断是否是空格
#         elif line.isspace():
#             dic['space']+=1
#         else:
#             dic['other']+=1
#     return dic
# #有返回值的必须赋值回来
# res=count("12345 &*%$ ABCabc")
# print(res)

'''
2、写函数,判断用户传入对象(字符串、列表、元组)的长度是否大于5
知识点：print(f"***")前的f,功能类似于{}.format一样
加f之后{}中的内容可以变化
'''
# def check_len(obj):
#     if len(obj)>5:
#         print(f'{obj}的长度大于5')
#     else:
#         print(f"{obj}小于5")
# check_len([1,2,3,4,5,6])
# check_len((1,[12,34,56,78,1],{'k'"1"}))
# check_len("hello world")

'''
3、写函数，检查传入列表的长度，如果大于2，
那么仅保留前两个长度的内容，并返回给调用者
或奇数位索引
'''
# def check_list_len(list):
#     if len(list)>2:
#         return list[:2] #0,1
#         # return list[1::2]
#
# res=check_list_len(['aaa','bbb','ccc','dddd'])
# print(res)
#
# res2=check_list_len(['123',345,(12,),'aa','bb'])
# print(res2)

'''
# 遍历字典列表dic.items()
for key,values in  dic.items():
    print key,values
'''
# def check_dic(dic):
#     for key,values in dic.items():
#         if len(values)>2:
#              dic[key]=values[:2] #是将key对应的value给切割了
#     return dic
# dic={"k1":"v1v1","k2":[11,22,33,44]}
# res=check_dic(dic)
# print(res)


'''
知识点复习：
1.格式化输出 %s
2.字典的格式化输出
'''
# print("he is %s friends" %("my"))
#
# dict={'name':'sunny','age':18,'sex':'male'}
# #匹配方式一
# print("value : %s" %(dict.get('sex')))
# #匹配方式二
# print(f"value : {dict.get('name')}" )

'''5、格式化输出'''
# students=[
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':38,'sex':'famale'},
#     {'name':'wxx','age':38,'sex':'famale'},
#     {'name':'yuanhao','age':58,'sex':'male'},
#     {'name':'liwen','age':68,'sex':'famale'},
# ]
# for i in students:
#     dic={}
#     for key,value in i.items():
#         dic[key]=value
#     print(f'<name:{dic.get("name")} age:{dic.get("age")} sex:{dic.get("sex")}>')

'''
题目：
1、移除值两边的空格 str.strip()
2、判断字符串是否以"al"开头 str.startswitch("al")
3、判断字符串是否以"X"结尾 str.endswitch("al")
4、将str中的'l'替换成'p' str.splace("l","p")
5、将str以'l分割 str.split("l")
6、将str中的小写变大写 str.upper()
7、将str中的大写变小写 str.lower()
8、输出str的第2个字符 str[1]
9、输出str的前3个字符 str[:3] #0 1 2
10、输出str的后个字符 str[-3:]
11、输出str对应"e"字符的索引位置 str.index('e')
12、获取子序列，去掉最后一个字符。如：oldboy 则获取 oldbo str[:-1]
'''

'''
两个集合
L1={'hello','web','python','linux'}
L2={'hi','web','js','java','python'}
1、即在L1又在L2中的元素     print(L1 & L2)
2、在L1或在L2中的元素       print(L1 | L2)
3、在L1但不在L2中的元素     print(L1 - L2)
4、不同时在L1和L2中的元     print(L1 ^ L2)
'''
# L1={'hello','web','python','linux'}
# L2={'hi','web','js','java','python'}
# print(L1 & L2)
# print(L1 | L2)
# print(L1 - L2)
# print(L1 ^ L2)

# msg_dic={
#     'apple':10,
#     'tesla':1000,
#     'mac':22,
#     'lenno':2889,
#     'chicken':55
# }
# dic={}
# for k,v in msg_dic.items():
#     dic[k]=v
# print(dic)
#
# '''有列表l=['a','b','l','a','a']去重，有序，无序'''
# #无序
# l=['a','b','l','a','a']
# new_list=list(set(l))
# print(new_list)
#
# #有序去重
# l=['a','b','l','a','a']
# new_list=[]
# for ele in l:
#     if ele not in new_list:
#         new_list.append(ele)
# print(new_list)

# def func(x,y,*,a,b):
#     print(x,y,a,b)
# func(1,2,a=3,b=4)
# func(1,2,b=4,a=3)
# #func(1,2,3,4) 报错
# #func(1,2) 报错


'''知识：名称空间,输入的foo()结果为1，
    原因是：以函数定义阶段为准，与调用位置无关
'''
# x=1
# # def func():
# #     print(x)
# def foo():
#     x=222
#     print(x)
# foo() #1

# #LEGB(方便记忆的函数名称)
# #bulit-in 内建函数
# #global 全局变量
# def f1():
#     #enclosing 内部函数
#     def f2():
#         #enclosing 内部函数
#         def f3():
#             #local 先从本地找
#             pass


'''
global的用法：
#1).示例一：全局的x与局部的x并不会发生任何关系
'''
# x=111
# def func():
#     x=222
# func() #执行函数后输出x
# print(x)  #111

'''
#2).示例二：变量为不可变类型，局部变量中的x,
          想要修改全局变量中的x，关键字global
'''
# x=111
# def func():
#     global x
#     x=222
# func()
# print(x)  #222

'''
#3).示例三：变量为可变类型,并不需要global
'''
# l=[111,222]
# def func():
#     l.append(222)
# func()
# print(l) #[111, 222, 222]

'''
nonlocal的用法:修改当前函数的外层函数，(不可变类型)
#1)示例一：
'''
# x=0
# def func1():
#     x=11
#     def func2():
#         x=22
#         print(x)
#     func2()
# func1() #在func1()中调用func2() 22
# print(x) #这个x为全局中的x 0
'''#2)示例二：'''
# x=0
# def func1():
#     x=11
#     def func2():
#         global x #对全局变量进行了改变
#         x=22
#         print(x)
#     func2()
#
# func1() #在func1()中调用func2()  22
# print(x) #这个x为修改后的全局x  22

'''
需求：修改func2()外层函数中x的值,会一直往外层找，
    直到没有外层函数，若最外层函数还是没有会报错
'''
# x=0
# #函数定义
# def func1():
#     x=11
#     def func2():
#         nonlocal x #修改的当前函数外层的x
#         x=22
#         print("===x",x) #x=22
#     func2()
#     print("输出func1()中的x：",x) #22
# #函数执行
# func1()

'''
可变类型,依然可以直接添加
'''
# def f1():
#     x=[]
#     def f2():
#         x.append("str")
#     f2()
#     print("f1中的x",x)
#
# f1() #f1中的x ['str']


# x=1
# def func():
#     print(x)
# def foo():
#     x=222
#     func()
# foo()

# input=111
# def f1():
#     def f2():
#         input=333
#         print(input)
#     input=222
#     f2()
# input=3337
# f1()

# x=111
# def func():
#     print(x)
#     x = 222
#
# func() #报错 赋值前引用局部变量“ x”

# x=111
# def func():
#     print(x)
#     #x = 222
#
# func() #111
#
# x=111
# def func():
#     x = 222
#     print(x)
#
# func() #222


# def index(x,y):
#     print(x,y)
'''
过程：
    #1)形参中：*将多余的位置参数变成元组（111，222）
    #2)形参中：**将多余的位置参数变成字典{'a':333,'b':444}
    
    #3)实参中：*将元组(111,222)打散
    #4)实参中：**将{'a':333,'b':444}字典打散
    
    #5)调用wrapper函数,也就是说wrapper中的参数会原封不动的传给index
    #6)但是index定义时只能接收两个参数，因此会报错
    
应用：一个函数的参数要原封不动的传递给另一个参数
'''
# def wrapper(*args,**kwargs):
#     index(*args,**kwargs)
#
# wrapper(111,222,a=333,b=444)

# def index():
#     return 123
# def foo(func):
#     return func
# foo(index) #传函数时，传入的index不可以加括号


'''
装饰器如何使用：
原本是index一个函数，
现在我需要给index添加一个计算运行时间的功能
前期知识：
    python中有一个time模块
    time.sleep(x) 程序停x秒
    time.time() 计算从1970年开始到现在的秒数
    #1970年是unix元年
'''
# 1)原来的代码
# import time
# def index(x,y):
#     time.sleep(3)  # 因为一行代码时间太快了
#     print("index %s %s" %(x,y))
# index(111,222)


# 1)方案一：改变了代码结构
# import  time
#
# def index(x,y):
#     start = time.time()
#     time.sleep(3)
#     print("index %s %s" %(x,y))
#     end = time.time()
#     print(end - start)
# index(111,222)


# 2)方案二：改变了调用方式
# import time
# def index(x,y):
#     time.sleep(3)
#     print("index %s %s" %(x,y))
#
# def wrapper():
#     start=time.time()
#     index(111,222)
#     end=time.time()
#     print(end-start)
# wrapper()

# 3)方案三：方案二优化
'''index的参数写死了'''
# import time
# def index(x,y):
#     time.sleep(3)
#     print("index %s %s" %(x,y))
#
# def wrapper(a,b):
#     start=time.time()
#     index(a,b)
#     end=time.time()
#     print(end-start)
# wrapper(111,222)

# 4)在优化
'''
这样wrapper里的参数会原封不动的给index
但是需要遵循index的参数规则
'''
# import time
# def index(x,y):
#     time.sleep(3)
#     print("index %s %s" %(x,y))
#
# def wrapper(*args,**kwargs):
#     start=time.time()
#     index(*args,**kwargs)
#     end=time.time()
#     print(end-start)
# wrapper(111,222)

'''
二分法：前题；列表按大小排序的
如果没有顺序，先排序：num.sort()
'''
# nums=[-3,2,4,5,6,7,10,23,33,45,67,78]
# find_num=93
#
# def binary_search(find_num,l):
#     print(l)
#     if len(l)==0:
#         print("未找到")
#         return #结束函数
#     mid_index=len(l)//2   #py中//是得到整数
#     mid_val=l[mid_index]
#
#     if find_num>mid_val:
#         #查找右边,列表切片
#         l=l[mid_index+1:]
#         binary_search(find_num, l)
#     elif find_num<mid_val:
#         #查询左边,列表切片
#         l=l[:mid_index]
#         binary_search(find_num,l)
#     else:
#         print("find it")
#
# binary_search(find_num,nums)

'''
IndexError: list index out of range
L=[]
L[0]
这种情况会报错
'''

'''
调用模块foo
1、import ...
    首次导入模块会发生3件事情：
    (1)、执行模块
    (2)、产生模块的名称空间，将模块执行过程中产生的名字放入名称空间
    (3)、当前文件便产生一个该模块的名字，该名字指向名称空间

2、import XXX as XX2
给XXX起了个别名XX2
'''
# import foo
# print(foo.x)
# foo.change()
# print(foo.x)
# print(__name__)
'''
1、from...import...
    

2、from...import *(导入一个模块中的所有名字) 
    __all__
    文件中有__all__这个变量，这个变量中默认为列表形式，存入的是模块中的所有名称
    import * 中的*，即时根据__all__变量来找的名称
    也就是说，可以通过改变__all__来改变可导入的模块中的名字
3、也可以起别名
    from...import ... as ...
    
4、循环导入
    尽量不用，或者将变量封装到函数中
'''

'''
模块的搜索路径的优先级：
    因为导入的模块也是一个文件，因此存在模块路径问题
    1、内存(内置函数)
    2、硬盘(按照sys.path中存放的文件的顺序依次查找要导入的模块)
    
    sys：值为一个列表，存放一系列的文件夹 
    其中第一个文件夹是当前执行文件所在的文件夹
    
    3、了解：sys.modules可以查看以及加载到内存的模块
'''

# import sys
# print(sys.path)
# print(sys.modules)
#
# import foo #导入
# del foo  #解绑，但是解绑后foo仍然存在在内存中

'''
包：python package
1、包就是一个包含有__init__.py文件的文件夹
2、包的本质就是模块，可以用来导入
3、因为建的包是一个文件夹，但是运行时需要有一个来代替py文件的运行

但是包是一个文件夹，可以存入很多py文件，但是文件中的名字都需要在__init__文件中
疑问？如何导入进去
1、绝对导入：以包文件夹作为起始来进行导入
    但是会带来一个问题：
        如果是使用者来下载这个包，可能路径并不在当前文件夹下,也就是说并不在当前文件夹的sys.path中
        那么需要手动加入文件路径 sys.path.append(r‘路径’)

强调：
1).导入时带点的，点的左边是一个包
2).两个包有相同的名字不冲突
3).import导入文件，产生的名字来自文件本身，导入包，产生的名字来自__init__文件

2、相对导入(仅限包内使用，包内导入可使用)
    . 当前路径 
    .. 上一级路径
'''

# import pack
# import sys
# print(pack.x)
# print(sys.path)


'''
软件目录规范
-bin
    -start.py:项目启动入口
-conf
    -setting.py:存放固定的配置文件
-core
    -src.py:存放核心业务逻辑代码
-db
    -db_file
    -db_handler：用于存放操作数据的代码
-lib
    -common.py:存放公共方法

-log、
    -log.txt：日志文件
readme.txt:放置文件使用规范

-interface
    -user_interface.py:用户接口

https://blog.csdn.net/JOJOY_tester/article/details/54598713

'''
# import os
# os.path.dirname(__file__)


# print("运行结果为：")
# print(__file__) #当前文件夹的绝对路径
# import os
# #os.path.dirname(__file__) 当前文件夹的父级文件夹
# PATH1=os.path.dirname(__file__) #当前文件夹的父级文件夹
# PATH2=os.path.dirname(PATH1)
# print("第一个...")
# print(PATH1)
# print("第二 个...")
# print(PATH2)


'''
常用模块的使用：
    #一：time
    时间分为3种格式：
        1、时间戳：从1970年到现在经过的秒数
            作用：用于时间间隔的计算
        2、按照某种格式显示的时间：2020-03-30 11:11:11
            作用：用于展示时间
        3、结构化的时间
            作用：用于单独获取时间的某一部分
    #二：datetime
        
    #三：时间格式的转换
    
'''
# # #1)
# import time
# print(time.time())
#
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
#
# print(time.strftime('%Y-%m-%d %X'))
#
# res=time.localtime()
# print(res)
# print(res.tm_yday)
# #
# #2)
# import datetime
# print(datetime.datetime.now())
#
# #datatime的优点为可以进行时间计算
# #+为几天后，-为几天前
# print(datetime.datetime.now()+datetime.timedelta(days=3))

'''
1、时间格式的转换
struct_time--->时间戳
'''
# import time
# s_time=time.localtime()
# print(time.mktime(s_time))

'''
时间戳--->struct_time
#时间区别
'''
# import time
# tp_time=time.time()
# print(time.localtime(tp_time))
#
# #时间
# print(time.localtime())#北京 上海时间
# print(time.gmtime()) #世界标准时间
#
# print(time.localtime(333333)) #转化为上海时间
#
# print(time.gmtime(333333)) #转化为世界标准世界

'''
struct_time--->格式化的字符串形式
'''
# s_time=time.localtime()
# #默认第二个参数就是当地时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))
#
# '''
# 格式化的字符串形式--->struct_time
# '''
# print(time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S'))


'''
总结：需要掌握的只有一条
结构化字符串<----->时间戳
format string <-----> timestamp

例子:需求,'1988-03-03 11:11:11' 加7天之后重新存入
'''

# #format string --->struct_time --->timestamp
# struct_time=time.strptime('1988-03-03 11:11:11','%Y-%m-%d %X')
# timestamp=time.mktime(struct_time)+7*86400
# print(timestamp)
#
# #format string <---struct_time <---timestamp
# res=time.strftime('%Y-%m-%d %X',time.localtime(timestamp))
# print(res)

'''
了解知识:

%a %b %d %H %M %S %Y
'''
# #三种结果相同
# import time
# #转化当前时间
# print(time.asctime())
# print(time.ctime())
# #转化时间戳
# print(time.ctime(time.time()))
#
#
# import datetime
# print(datetime.datetime.now()) #本地时间
# print(datetime.datetime.utcnow())#世界时间
#
# #时间戳可以直接转化为格式化字符串时间
# print(datetime.datetime.fromtimestamp(3333))

'''
random模块
应用:随机验证码
'''
# import random
#
# print(random.random())#(0,1)----float    大于0且小于1之间的小数
#
# print(random.randint(1,3))  #[1,3]    大于等于1且小于等于3之间的整数
#
# print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数
#
# print(random.choice([1,'23',[4,5]])) #1或者23或者[4,5]
#
# print(random.sample([1,'23',[4,5]],2))#列表元素任意2个组合
#
# print(random.uniform(1,3))#大于1小于3的小数，如1.927109612082716
#
#
# item=[1,3,5,7,9]
# random.shuffle(item) #打乱item的顺序,相当于"洗牌"
# print(item)
'''
逻辑关系
for i in range(6):
     随机字符=random.choice([从数字中任取一个,从字母中任取一个])
     从数字中任取一个:str(random.randint(0,9))
          不可以直接用它是因为他得到的是整型,后面要与字符串做加法
          所以需要类型转化
     从字母中任取一个:
        小知识:内置函数转化工具
        chr(65) 将数字转化为对应的字符
        ord('A') 将字符转化为对应的数字
        chr(random.randint(68,90))
     res+=随机字符
'''
# 1).实现办法一:
# import random
# res=''
# for i in range(6):
#     s1=str(random.randint(0,9))
#     s2=chr(random.randint(65,90))
#     res+=random.choice([s1,s2])
# print(res)

# #2)如果想写成一个功能的话
# import random
# def make_code(size):
#     res=''
#     for i in range(size):
#         s1=str(random.randint(0,9))
#         s2=chr(random.randint(65,90))
#         res+=random.choice([s1,s2])
#     return res
# print(make_code(5))

'''
os
'''
# import os
# #获取某一个文件夹下所有的子文件以及文价夹的名字
# res=os.listdir('.')
# print(res)
#
# #得到文件大小(不是文价夹的大小)
# size=os.path.getsize(r'./test2.py')
# print(size) #单位是字节
#
# # #获取一个文件下的所有文件目录
# # os.system(r"dir")
#
# #得到的是字典类型,key和value都是字符串
# #PATH:执行系统命令时使用
# #sys.path:导入模块的环境变量
# print(os.environ)

# print(__file__)
# print(os.path.abspath(__file__))
# D:/mycode/CBOW/函数、import/test2.py
# D:\mycode\CBOW\函数、import\test2.py(根据平台获取路径)


# #将路径与文件名分开
# res=os.path.split('/a/b/c/d.txt')
# print(res)
#
# #获取路径名
# print(os.path.dirname(r'a/b/c/d.txt'))
# #获取文件名
# print(os.path.basename(r'a/b/c/d.txt'))
#
# #判断是否时决定路径
# print(os.path.isabs('/a/b/c')) #True
#
# #判断文件是否存在(不是文件夹)
# print(os.path.isfile(r'../123.png'))
# #判断文件夹是否存在
# print(os.path.isdir(r'../pack'))
#
# #路径拼接
# print(os.path.join('a','b','c','d')) #a\b\c\d(与路径有关)
#
# print(os.path.join('a','/','b','c','d')) #/b\c\d
#
# print(os.path.join('a','C:','b','c','d')) #C:b\c\d


'''
sys模块
应用：打印进度条
[##########] 100%

小知识：格式化
[%-50s]
长度为50，左对齐
'\r'为不换行，每次冲行首打印
打印% ，%%
'''
# sys 可以拷贝文件

# import time
# res=''
# for i in range(50):
#     res+='#'
#     time.sleep(0.5)
#     print('\r[%-50s]'%res,end='')


# #模拟进度条的功能
# import time
# recv_size=0
# total_size=103473
#
# while recv_size<total_size:
#     recv_size+=1024
#     percent=recv_size/total_size
#     if percent>1:
#         percent=1
#     res=int(percent*50)*'#'
#     time.sleep(0.01)
#     print('\r[%-50s] %d%%' %(res,percent*100), end='')


# #模拟进度条的功能
# import time
# recv_size=0
# total_size=103473
#
# #功能函数形式
# def progress(percent):
#     if percent > 1:
#         percent = 1
#     res = int(percent * 50) * '#'
#     time.sleep(0.01)
#     print('\r[%-50s] %d%%' % (res, percent * 100), end='')
# while recv_size<total_size:
#     recv_size+=1024
#     percent=recv_size/total_size
#     progress(percent)


'''
shutil模块:
    拷贝文件
'''
