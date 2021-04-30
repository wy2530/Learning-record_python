"""
用类实现的装饰器：property

property：是一个装饰器，是将功能属性转换为数据属性
"""


# 应用案例1（体质）：

# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     '''
#     因为BMI是计算出来的，所以需要单独写一格函数，不然会写死
#     但是在用户看来BMI又属于数据属性，需要之间查看，因此需要用到property属性
#     '''
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj1 = People("WY", 45, 1.57)
# # print(obj1.bmi())
# '''
# 加property与不加的区别：
#     没有加装饰器时，BMI是一个函数，你需要调用函数，因此需要加括号
#     加装饰器后，BMI是一个数据属性，访问属性，不需要加括号的
# '''
# print(obj1.bmi)


# 应用案例二：
class People:
    def __init__(self, name):
        self.__name = name

    @property  # get_name=property(get_name)
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, val):
        if type(val) is not str:
            print("输入必须为字符串")
            return
        self.__name = val

    @get_name.deleter
    def del_name(self):
        print("不可删除")

    # name=property(get_name,set_name,del_name)
obj1 = People("hello")

# obj1.set_name("aaa")

# print(obj1.get_name)

del obj1.del_name

'''
对于使用者来说：
    调用删、改、查 更像是一个功能
那么如何使它更像一个数据呢？
两种办法：
    1、name=property(get_name,set_name,del_name)
    2、将功能函数的名字都改成name
      定义@property
         @name.setter 设置
         @name.deleter 删除
         

'''

'''
问题：到底什么时候用print
'''
