"""
面向过程：
    程序流程化
面向对象：
    对象是 “容器”，盛放数据和功能
    程序 ”整合“
"""

'''

__init__

调用类的过程又称之为实例化，发生了三件事：
1、先产生一个空对象类中的
2、python会自动调用类中的__init__方法，然后传参给函数
3、返回初始化完的对象


总结__init__方法：
1、会在触发时自动触发执行，用来为对象初始化自己独有的数据
2、__init__内存应该存放 是为对象独有的属性
3、必须返回一个None值，不能是其他类型
'''
# class Student:
#     count=0
#     def __init__(obj,x,y,z):
#         Student.count=+1;
#         obj.stu_name=x;
#         obj.stu_age=y;
#         obj.stu_gender=z;
#         # return None

'''
类中存放的是对象公有的数据与功能
类可以访问：数据属性+函数属性

类的函数属性是绑定给 对象 用的,
虽然函数指向的都是相同的功能，但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同
id()可以查地址


要求：
每实例化一次，数量+1，也就是查看对象的数量
需要在建立对象的时候直接加1，可以在__init__里面加属性，
但是不可以在写obj对象，而是应该写 类.数量+1

__dict__

例如：建立了一个学生类，在类中使用__init__方法和其他函数，创建了不同的实例对象
那如果你想去使用函数的功能：两种办法，  类.函数   对象.函数

使用对象.函数()是绑定的功能，不同之处在于：
1、谁调用谁就是第一个参数，也就是说，不用传参 便可以找到对象中的所有功能
2、如果在类中定义了一个没有被传入参数的函数,那么使用对象，函数()去调用，他仍然会传入自己，
那么此时会出现，并不需要传参，你却传参了的错误。
3、比较习惯的参数命名，第一个都是以self==》自己
4、只是第一个参数不需要传递了，其他参数仍然需要
解决办法：1、无论是否使用，都需要先传一个参数
        2、后期可以使用装饰器去改变功能

使用类.函数()，想使用某个对象，就必须传参

类.函数====》地址
对象.函数===》绑定方法

# 想一想list：(前面的知识都是对象)
l=[1,2,3] #使用了功能list()
print(list)  #<class 'list'> 
也就是说list是一个类,l是你创建的一个list的实例
所以,你可以用l.XXX()去调用list里面的函数(方法)
不能使用l.0的原因是,list将.处理为了 l[0]
'''

'''
选课系统：
    名字：
    地址：
    
    班级名字：
    班级所在校区：#去掉
    
    学生的学校： #去掉
    学生的姓名、年龄、学号、性别
    
    课程名字、课程周期、课程价格
    
    老师的名字、年龄、薪资、职称 
    
功能部分：
    小区创建完毕后，可以为每个校区关联班级
    
    班级创建完毕后，可以为每个班级关联创建课程
    
    班级创建完毕后，可以为每个班级添加学生
     
    班级创建完毕后，学术可以选择课程、选择班级
    
'''


class School:
    school_name = "华北理工大学"

    # 学校的私有属性
    def __init__(self, nickname, address):
        # 学校的某个校区名字
        self.nickname = nickname;
        self.address = address;
        # 在学校内创建班级
        self.classes = []

    # '''
    # 修改前的相关属性
    # '''
    # # 学校的共有属性
    # def related_class(self, class_name):
    #     # 为学校的某个校区添加班级,也就是为对象添加班级
    #     self.classes.append(class_name)

    '''
    修改后的相关属性
    '''

    # 学校的共有属性
    def related_class(self, class_obj):
        # 为学校的某个校区添加班级,也就是为对象添加班级
        # 此时classes是关于班级的列表
        self.classes.append(class_obj)

    # '''
    # 修改前的查看
    # '''
    # # 查看某个校区开设了哪些课程
    # def tell_class(self):
    #     print("%s" % self.nickname)
    #     for info in self.classes:
    #         print("    %s" % info)

    '''
    修改后的查看
    '''

    # 查看某个校区开设了哪些课程
    def tell_class(self):
        print(self.nickname)
        # 从班级里找该对象的课程信息
        for class_obj in self.classes:
            class_obj.tell_course()


# 实例化，创建学校校区：名字+地址
school_obj1 = School("华北理工大学曹妃甸校区", "唐山")

school_obj2 = School("华北理工大学老校区", "北京")

# 为学校开设班级
'''
曹妃甸校区 
    计算机科学与技术
    材料成型

老校区
   机械工程
   临床医学
'''


# school_obj1.related_class("计算机科学与技术")
# school_obj1.related_class("材料成型")
#
# school_obj2.related_class("机械工程")
# school_obj2.related_class("临床医学")


# 要求：查看每个校区内开设了哪些班级

# print("============")
# school_obj1.tell_class()
# print("============")
# school_obj2.tell_class()
# print("============")
# print("            ")


class Class:

    # 班级独有的东西 班级名、班级编号、班级里面应该有的课程名
    def __init__(self, name, class_id):
        self.name = name
        # 班级编号
        self.id = class_id
        # 班级课程
        self.course_obj = []

    # 向班级中添加课程名
    def related_course(self, course_obj):
        self.course_obj.append(course_obj)

    # # 向班级中添加课程名
    # def related_course(self, course_obj):
    #     self.course_name.append(course_obj)

    # 班级中有多少课程
    '''
    计算机科学与技术
        网络原理
        软件工程
    机械工程
        机械制图
        CAD
    '''

    def tell_course(self):
        print("班级名：%s" % self.name)
        for info in self.course_obj:
            info.tell_course_info()


class_obj1 = Class("计算机科学与技术", "1466")

class_obj2 = Class("机械工程", "1403")

class_obj3 = Class("材料成型", "1422")

# # 为班级开设课程
# class_obj1.related_course("网络原理")
# class_obj1.related_course("软件工程")
#
# class_obj2.related_course("机械制图")
# class_obj2.related_course("CAD")
#
# class_obj3.related_course("高等数学")
# class_obj3.related_course("线性代数")

'''
曹妃甸校区
    计算机科学与技术
        网络原理
        软件工程
    材料成型
        高等数学
        线性代数
        
老校区
    机械工程
        机械制图
        CAD
'''
# # 查看班级需要上的课程有哪些
# print("============")
# class_obj1.tell_course()
# print("============")
# class_obj2.tell_course()
# print("============")


'''
在班级和学校之间建立联系：
   将学校的共有属性 related_class 中传的参数直接改为 课程对象 即可
'''
# 校区1的班级
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj3)

# 校区2的班级
school_obj2.related_class(class_obj2)

# print(school_obj1.classes)

# school_obj1.tell_class()
# print("========")
# school_obj2.tell_class()

# 课程信息课程名字、课程周期、课程价格
'''
网络原理 
    60天
    1200
软件工程
    45天
    1000
'''


class Course:
    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price

    def tell_course_info(self):
        # for course_obj in self.course_info_list:
        print("   课程名：%s \n   课程时间：%s \n   课程价格：%s \n" % (self.course_name, self.course_period, self.course_price))


course_obj1 = Course("网络原理", '60天', '1200')
course_obj2 = Course("软件工程", '45天', '1000')

course_obj3 = Course("线性代数", '45天', '1000')
course_obj4 = Course("高等数学", '45天', '1000')
# course_obj1.tell_course_info()

# 为班级开设课程
class_obj1.related_course(course_obj1)
class_obj1.related_course(course_obj2)

class_obj2.related_course(course_obj4)
class_obj2.related_course(course_obj3)
class_obj1.tell_course()
class_obj2.tell_course()
# school_obj1.tell_class()
# school_obj2.tell_class()
# course_obj1.tell_course_info()

'''
步骤
1、建立类的私有属性
2、建立类的实例对象
3、可打印的方法
4、对象调用方法

5、建立关联功能
'''

'''
封装： 

新功能：将封装的属性进行隐藏操作

1、如何隐藏：在属性名前加__前缀，就会实现一个对外隐藏属性效果
   
   隐藏功能对外不对内，因为__开头的属性在运行前 都会 发生变形
     这种变形操作只在检查类语法的时候会发生一次变形，其他都不会发生变化
 
2、为何要隐藏
'''


class Foo:
    __x = 1

    def _f1(self):
        print("from Foo")

    # 内部可以访问
    def f2(self):
        print(Foo.__x)


# 访问类的名称空间
print(Foo.__dict__)
# 外部访问类名(会报错，找不到)
# print(Foo.__x)

print(Foo.f2)

# 平常写的Foo.XXX,都是在寻找名称空间里的key值 XXX
