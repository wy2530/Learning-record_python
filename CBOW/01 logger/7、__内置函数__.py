# obj1=int(10)
# print(obj1)
#
# print(obj1.__str__())

"""
关于带有__XXX__的内置方法：（常用）
    1、__str__
    2、__del__
"""


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def say(self):
    #     print('<%s:%s>'

    def __str__(self):
        return '<%s %s>' % (self.name, self.age)


obj = Foo("lili", 19)
print(obj)  # 我打印自定义对象obj看到的是地址

res = int(10)
print(res)  # 打印内置函数int不是地址，而是值

'''
其实打印的都是XXX.__str__中的内容
'''
print(obj.__str__())
print(res.__str__())

'''
那如何给自定义函数设置__str__呢?
'''
print(obj)