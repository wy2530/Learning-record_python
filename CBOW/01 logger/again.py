class School:
    school_name = "华北理工大学"

    # 学校的私有属性
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address

        # 为学校实例创建班级(班级列表)
        self.class_list = []

    def related_class(self, class_obj):
        self.class_list.append(class_obj)

    # 学校中有几个班级
    def tell_class(self):
        print(self.school_name)
        for class_info in self.class_list:
            class_info.tell_course()


class Class:
    def __init__(self, class_name):
        self.class_name = class_name
        # 一个班级有很多课程
        self.course_list = []

    def related_course(self, course_obj):
        self.course_list.append(course_obj)

    def tell_course(self):
        print(" 班级名：%s" % self.class_name)
        for course_info in self.course_list:
            course_info.tell_course_info()


class Course:
    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price

    def tell_course_info(self):
        print("      ")
        print("    课程名字：%s\n    课程周期：%s\n    课程价格：%s" % (self.course_name, self.course_period, self.course_price))


class Student:
    pass


# 建立一个学校对象实例
school_obj1 = School("华北理工大学曹妃甸校区", "曹妃甸")
# 学校1有两个班级
class_obj1 = Class("计算机科学与技术")
class_obj2 = Class("人工智能与自动化")

# 班级1有两讲课
course_obj1 = Course("网络原理", "60天", "1000")
course_obj2 = Course("软件工程", "60天", "1200")

# 班级2有两讲课
course_obj3 = Course("python开发", "60天", "1500")
course_obj4 = Course("Linux运维", "60天", "800")

# 班级1与课程建立关联
class_obj1.related_course(course_obj1)
class_obj1.related_course(course_obj2)

# 班级2与课程建立关联
class_obj2.related_course(course_obj3)
class_obj2.related_course(course_obj4)

# 学校1与两个班级建立关联
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj2)

# 查看学校1中班级、课程有哪些
# school_obj1.tell_class()

# 查看学校1的 班级1 中有哪些课程
class_obj1.tell_course()
