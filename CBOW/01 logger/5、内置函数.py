# ======》掌握
"""
dir 查看一个对象或类能点出来哪些属性
"""


class Foo:
    pass


obj = Foo()
print(dir(obj))  # obj.XXX

'''
# 计算10除以3的商和余数
一般在计算分页的时候使用
'''
print(divmod(10, 3))

'''
enumerate：既可以拿到索引也可以拿到值
'''
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)

'''
eval:执行字符串中的表达式，并给一个返回值
注意：本来是字符串的
'''
res = eval('1+2')
print(res)

res1 = eval('{"a":1}')  # 字符串就会变成字典类型
print(res1, type(res1))

'''
set：可增加、删除、修改的集合
frozenset:不可变集合
'''
x = set({1, 2, 3})
x.add(4)
print(x)
s = frozenset({1, 2, 3})

'''
isinstance:是用来判断一个对象是不是一个类的实例的
但是在Python3中统一了类与类型的概念，也就是说，
可以用它来判断XXX是不是什么什么类型
'''


class Foo:
    pass


obj = Foo()
print(isinstance(obj, Foo))  # True
print(isinstance([1,2,3],list)) # True


'''
zip:将两个可迭代的对象一一对应，拼接成一个元组
'''
v1='hello'
v2=['1',2,2.3,'{1,2}',"111"]
res=zip(v1,v2)
print(res)
print(list(res))

'''
关于模块导入：
'''
import time  #我们平时导入的时候import后面的模块都不是字符串
time.sleep(3)
# 如何是字符串怎么导入呢？ #效果相同
x=__import__('time')
x.sleep(3)
# ==========》了解

# 取绝对值的函数
print(abs(-1))
'''
all  可以自己看解释
#如果可迭代对象是空，返回True,如果循环中有值，那必须所有值都为真才是真
'''
print(all([]))  # True
print(all([1, 2, '']))  # False

'''
any  可以自己看解释
#如果可迭代对象是空，返回False,如果循环中有值，那任意值为真就可以是真
'''
print(any([]))  # False
print(any([1, 2, '']))  # True

'''
进制转换
'''
# 10--->2
print(bin(11))
# 10--->8
print(oct(11))
# 10--->16
print(hex(11))

'''
判断某一个变量对应的值可不可以被调用
'''


def fun():
    pass


print(callable(fun))  # 不用加(),加括号就是调用了

'''
ASCII数字字母的转换
'''
print(chr(65))
print(ord('A'))
