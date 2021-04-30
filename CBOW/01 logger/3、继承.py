'''
继承：
    创建新类的方式
    python支持多继承

python的多继承：
    优点：子类可以同时遗传多个父类的属性，最大限度地重用代码
    缺点：
        继承表达的是一种什么“是”什么的关系
        但是多继承可能有些别扭
        1、违背了思维习惯
        2、代码可读性变差
        3、扩展性变差
    如果真的涉及到一个子类不可避免地要重用多个父类的属性，应该使用 Mixins
'''


class Parent1:
    pass


class Parent2:
    pass


class Sub1(Parent1):  # 单继承
    pass


class Sub2(Parent1, Parent2):  # 多继承
    pass


# 查看子类继承的父类
# print(Sub1.__bases__)
# print(Sub2.__bases__)
#
# print(Parent1.__bases__)
'''
在python2中有经典类和新式类之分
    新式类：继承了object类的子类，以及该子类的子类
    经典类：没有继承继承object类的子类，以及该子类的子类
在python3中全是新式类，即没有继承任何类的，默认继承object类
    
若想py3和py2兼容，需要将Python3中，所有没有继承的类都添加一个object
    class Parent1(object):
        pass
    class Parent2(object):
        pass
'''

'''
类：解决对象与对象之间的代码冗余问题
继承：解决类与类之间的代码冗余问题
'''

# class student:
#     school = "华北理工大学"
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def choose_course(self):
#         print("学生 %s 正在选课" % self.name)
#
#
# obj_stu = student("hello", 18, 'female')
# obj_stu.choose_course()
#
#
# class teacher:
#     school = "华北理工大学"
#
#     def __init__(self, name, age, sex, level, salary):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.level = level
#         self.salary = salary
#
#     def good_teacher(self):
#         print("%s是好老师" % self.name)
#
#
# obj_tea = teacher("liming", 18, 'male', '教授', '薪水')
# obj_tea.good_teacher()


'''
综上：可发现问题：有重复的属性
那么我们可以知道 继承就是为了解决类与类之间的重复问题的
3、那么如何使用继承呢?
有两种情况：
    1、子类完全继承父类的函数
    2、子类只用了父类函数的一部分
'''


# 首先我们抽象出来一个人的属性
class People:
    school = "华北理工大学"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 子类中的函数与父类函数完全相同是,只需添加独有的功能即可
class student(People):

    def choose_course(self):
        print("学生 %s 正在选课" % self.name)


obj_stu = student("hello", 18, 'female')


# obj_stu.choose_course()


class teacher(People):
    school = "华北理工大学"

    def __init__(self, name, age, sex, level, salary):
        # 子类与父类属性不完全相同时的做法
        People.__init__(self, name, age, sex)

        self.level = level
        self.salary = salary

    def good_teacher(self):
        print("%s是好老师" % self.name)


obj_tea = teacher("liming", 18, 'male', '教授', '薪水')


# obj_tea.good_teacher()


# 单继承背景下的属性查找
# 示范一：子类自己有的先找自己
class Foo:
    def f1(self):
        print("Foo.f1")

    def f2(self):
        print("Foo.f2")
        self.f1()


class Bar(Foo):
    def f1(self):
        print("Bar.f1")


#
# obj = Bar()
# obj.f2()


# Foo.f2
# Bar.f1

# 示范二:
class Foo:
    def f1(self):
        print("Foo.f1")

    def f2(self):
        print("Foo.f2")
        # 要求这个必须访问Foo
        # self.f1()
        Foo.f1(self)  # 方法一：此时self就是Foo了


class Bar(Foo):
    def f1(self):
        print("Bar.f1")


#
# obj = Bar()
# obj.f2()


# 示范三:
class Foo:
    def __f1(self):
        print("Foo.f1")

    def f2(self):
        print("Foo.f2")
        # 要求这个必须访问Foo
        self.__f1()  # 方法二：使用隐藏属性 _Foo__f1


class Bar(Foo):
    def __f1(self):  # _Bar__f1
        print("Bar.f1")


#
# obj = Bar()
# obj.f2()


'''
多继承：
1、什么是菱形问题
       D继承了B,A两个或多个父类
       B,A两个或多个父类又同时继承了一个相同的非object的父类
       （因为在python3中，所有的类都继承于object）
    
2、菱形问题的继承原理：
    对于我们定义的类，无论这个类是否继承（因为有默认的object继承）
    python会通过一个算法计算出 一个方法解析顺序的列表，也就是MRO列表。
    该列表就是多继承的查找顺序，通过从左到右不断查找，直到找到，找不到会报错
    (MRO是类有的，对象没有)
    
    类和类的对象访问属性都是参照该类的mro列表

排列法则：
    先查找子类本身
    按父类继承顺序查找
    如果父类有两个父类，先找第一个父类，具体查看一下MRO
    
    
3、非菱形继承：
    python2与python3（经典类和新式类）是相同的，是按分支查找的
    先找完一个父类的分支，再找下一个父类的分支
    
将没有继承的类，写一下继承object类，会兼容py2

菱形类，py2和py3经典类和新式类）是有区别的,
    当py2中的G没有继承object的时候，是经典类，
    经典类：深度优先，会在检索 第一条分支的时候 之间找到黑，会检索到共同的父类
    新式类：广度优先，在检索 最后一条 分支的时候  才会检索到共同的父类
'''


# 2问题示例：

class A:
    def test(self):
        print("from A")


class E:
    def test(self):
        print("from E")


class G(A):
    def test(self):
        print("from E")


class B(E, G):
    def test(self):
        print("from B")


class C(A):
    def test(self):
        print("from C")


class D(B, C):
    pass


obj = D()


# obj.test()  #from B
#
#
# print(D.mro())  # D-B-E -G -C-A -object


class F:
    def test(self):
        print("from F")


class E:
    def test(self):
        print("from E")


class D:
    def test(self):
        print("from D")


class B(E):
    def test(self):
        print("from B")


class C(F):
    def test(self):
        print("from C")


class A(B, C, D):
    pass


obj = A()
# obj.test()  #from B
#
#
# print(A.mro())  # A-B-E  -C-F  -D-object


'''
继承结构不能过复杂
要在多继承的背景下满足继承的关系===》mixins

1、什么是mixins?
    是一种书写规范，使多继承更可读
2、满足什么“是”什么
'''

# Mixins示例：
'''
对于民航飞机、直升飞机、汽车来说，都属于交通工具
但是飞机可以飞，汽车不行，所以可以从民航飞机、直升飞机中提取出飞行的父类
但是这样会导致可读性变差，那么使用变量名规范的格式，用来区分是父类还是另外的功能类
一般来讲，父类放在最右边
'''


class Vehicle:  # 交通工具(父类)
    pass


class FlyableMixin:  # 功能类
    pass


class CiviAircraft(FlyableMixin, Vehicle):  # 民航飞机
    pass


class Helicopter(FlyableMixin, Vehicle):  # 直升飞机
    pass


class Car(Vehicle):  # 汽车
    pass


'''
在子类派生的新方法中如何重用父类的功能
方式一：指名道姓调用某一个类下的函数--》不依赖于继承关系
方式二：super()调用父类提供给自己的方法--》严格依赖依赖继承关系
'''


# 方式一：指名道姓调用某一个类下的函数--》不依赖于继承关系
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        People.__init__(self, name, age, sex)
        self.level = level
        self.salary = salary

#
# tea_obj = Teacher("hello", 18, 'male', '讲师', '1200')
# print(tea_obj.__dict__)


# 方式二：super()调用父类提供给自己的方法--》严格依赖依赖继承关系
#        调用super()会得到一个特殊的对象，该对象会参照 属性查找发起者 的mro,去访问当前类的父类中找属性
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        '''
        在Python2中需要传自己的类和对象，Python3什么都不需要
        '''
        super().__init__(name, age, sex)  # 注意：不用传self了，调用的是方法，自动传参（不理解背过即可）
        # super(Teacher,People).__init__(name, age, sex)
        self.level = level
        self.salary = salary


tea_obj = Teacher("hello", 18, 'male', '讲师', '1200')
# print(tea_obj.__dict__)
# 该对象会参照当前类的mro,去访问当前类的父类中找属性
# 也就是说会从第二个类开始找
# print(Teacher.mro())

'''
super:
    
'''
class  A:
    def test(self):
        print("from A")
        super().test()
class B:
    def test(self):
        print("from B")

class C(A,B):
    pass

obj=C()
obj.test()
'''
输出：
    from A
    from B
过程：
    1、首先是C调用的test()
    2、C中没有test()
    3、去C的父类中查找test(按mro的规则来说，第一个查找的父类是A)
    4、A中有test()，执行。
    5、第一行执行结果为 from A
    6、super() 应该找的是属性发起者的父类，也就是C的父类A，A再找他的父类中的属性
    7、矛盾点就是：肉眼看B不属于A的父类，但是在MRO中来看，B是A的父类，所以在B里找了
    
    8、为什么找了两次父类？
        类比上一个例子，在Python2中华需要放的是
        super(Teacher,self) , 但是我们的需求是找Teacher父类中的属性
'''
print(C.mro())  #C-A-B-object




'''
组合：
    class_obj.course=course_obj  #一个类中的属性 等于了另一个对象
'''