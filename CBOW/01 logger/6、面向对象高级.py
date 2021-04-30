# 反射
# 内置方法
# 元类

'''
python是动态语言，用的时候才会去获取信息
什么是反射？（是Python的分析的一种能力）
    指的是在程序运行的过程中可以”动态“获取
'''


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s:%s>' % (self.name, self.age))


obj = Foo("lili", 19)

# 1、先通过dir,查看出某个对象下可以点出哪些属性
print(dir(obj))

# print(obj.__dict__[dir(obj)[-2]])
'''
但是通过dir获取到的属性都是字符串格式的
那么python有4个内置属性，可以通过字符串来操作属性

可以通过上述__dict__的方法去操作，但是非常有局限
因为不是所以属性都有__dict__方法，另外，属性的索引也不确定
'''

# 判断属性有没有
print(hasattr(obj, 'name'))  # True
# 得到
print(getattr(obj, 'name'))
# 修改
setattr(obj, 'name', 'wy')
# 查看是否修改
print(getattr(obj, 'name'))
# 删除
# delattr(obj,'name')
# 查看是否删除
print(obj.__dict__)

res = getattr(Foo, 'say')  # Foo.say #function
print(res)
res2 = getattr(obj, 'say')  # bound method
print(res2)

# res=getattr(obj,'name')
# print(res)

# obj=Foo("Hello")
# print(obj.name)
#
# res=obj.name
# print(res)


'''
反射案例：
    
'''
# 判断是否存在
print(hasattr(10, 'x'))  # False
# 如果不写None，也就是没有默认值了，在10下面没有X这个属性的时候就会报错
# 为了不报错，加上默认值None
print(getattr(10, 'x', None))
# 写了None,Foo在有say这个属性，会正常获取
print(getattr(Foo, 'say', None))

'''
案例：
    文件上传、下载和交互
'''


class Ftp:
    def put(self):
        print('正在上传...')

    def get(self):
        print('正在下载...')

    def interactive(self):
        method = input("请输入你想用的功能：").strip()

        # 因为input出来的是一个字符串,不能直接self.method
        if hasattr(self, method):
            getattr(self, method)()
        else:
            print("该功能不存在")

obj_ftp=Ftp()
obj_ftp.interactive()



