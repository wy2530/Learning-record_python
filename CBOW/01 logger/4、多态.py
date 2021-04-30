"""
1、什么是多态：同一事物的多种形态
"""


# Animal这种事物分了People、Dog、Pig多种

class Animal:
    pass


class People(Animal):
    pass


class Dog(Animal):
    pass


class Pig(Animal):
    pass


'''
2、为什么要有多态？======>多态可以带来什么特性？
    父类有的子类都有，也就是继承的另一种名称说法
    多态可以在不考虑对象具体类型的情况下，直接使用对象
'''


class Animal:
    def say(self):
        print("动物发声", end=' ')


class People(Animal):
    def say(self):
        super().say()
        print("嘤嘤嘤")


class Dog(Animal):
    def say(self):
        super().say()
        print("汪汪汪")


class Pig(Animal):
    def say(self):
        super().say()
        print("哼哼哼")


obj1 = People()
obj2 = Dog()
obj3 = Pig()

obj1.say()


# 使用多态可以提供统一的接口
def Animal_say(object):
    object.say()


Animal_say(obj2)

'''
以上那种统一的对象：可以想一想之前Python的函数
比如：len(__len__), for(__iter__)
    他们可以操作很多类型
（不同类型都有统一的接口名）
'''

print('hello'.__len__())
print([1, 2, 3].__len__())
print({'a': 1, 'b': 2}.__len__())


# 统一接口名
def my_len(val):
    return val.__len__()


# print(my_len('hello'))

'''
3、但是在Python中，比较推崇的不是以继承来体现多态
Python更推崇的是鸭子类型：不需要继承（一些类之间可以没有关系），做的像即可

'''


class Animal:
    def say(self):
        print("动物发声", end=' ')


class People:
    def say(self):
        super().say()
        print("嘤嘤嘤")


class Dog:
    def say(self):
        super().say()
        print("汪汪汪")


class Pig:
    def say(self):
        super().say()
        print("哼哼哼")


'''
4、抽象基类(了解)：
    使用父类来规范子类
因为有时，即使子类不写继承了父类，也可以做出效果，为了进行强制
有了抽象基类的用法，如果子类不写父类的方法，就会报错
'''

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        print("动物发声", end=' ')

    @abc.abstractmethod  # 不加这个装饰器时可以不定义
    def test(self):
        print("test")


# obj=Animal()  不可以实例化抽象类自己

class People(Animal):
    def say(self):
        print("嘤嘤嘤")

    def test(self):
        pass


class Dog(Animal):
    def say(self):
        super().say()
        print("汪汪汪")


class Pig(Animal):
    def say(self):
        super().say()
        print("哼哼哼")


obj1 = People()
# obj1.test()


'''
绑定方法：特殊之处在于谁调用谁就是第一个参数
    1、绑定给对象的方法：调用者是对象，传入的也是对象
    2、绑定给类的方法：调用着是类，传入的是类
    
非绑定方法：也就是单纯的函数，不可以自动传参
'''

import settings


class Mysql:
    def __init__(self, ip, port):
        # self.ip = ip
        self.ip=self.creade_id()
        self.port = port

    # self传入的是对象
    def fun(self):
        print('%s %s' % (self.ip, self.port))

    @classmethod  # 将下面的函数装饰成绑定给类的方法
    def my_sql(cls):
        return cls(settings.IP, settings.PORT)

    @staticmethod  # 将下述函数装饰成一个静态方法
    def creade_id():
        import uuid
        return uuid.uuid4()


# 绑定给对象的
obj = Mysql("128.128.1.1", 8806)
obj.fun()

# 绑定给类的
# 现在有一个需求，就是端口后要存外部文件中传入
obj2 = Mysql.my_sql()
# 从配置文件中读内容
print(obj2.__dict__)

# 非绑定类型，谁都可以调用的（可以没有参数,也可以有参数）
obj3=Mysql.creade_id()
print(obj3)