'''
元类的引入：
    一切皆对象

1、什么是元类：
    元类就是用来 实例化类的 类
关系：
    元类---实例化---》类 ----实例化----》对象
'''
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s:%s>' % (self.name, self.age))


# 造对象的步骤：调用类() , 赋值给对象
obj=People("bili",16)
# 造类的步骤：是一样的，调用类() , 赋值给类
# People=调用类

'''
但如何查看调用的是哪个类呢？
'''
# 查看对象的类:可以看到是people
print(type(obj))  # <class '__main__.People'>
# 查看类的类；type
print(type(People)) # <class 'type'>

'''
那我们可以知道了：
    type是内置的元类
    我们用class关键字定义的所有类以及内置的类都是由元类type实例化产生的
那我们接着来学一下class的机制分类
'''

'''
3、class关键字创造类的步骤
4、自定义元类
'''

