"""
返回无穷多的值
"""

# def function():
#     print("执行函数体")
#     return 1

'''
可返回 多次值的

如何得到一个自定义的迭代器:
    在函数内一旦有yield关键字，那么调用函数时，并不会执行函数体代码
    而是会有一个返回值，这个返回值是一个生成器，生成器也就是迭代器对象
    使用迭代器对象，g.__next__()
'''

def func():
    print("第一次")
    yield 1
    print("第二次")
    yield 2
    print("第三次")
    yield 3
    print("第四次")


'''
g现在是迭代器对象，也就是生成器
'''
g=func()

'''
g.__next__()会触发函数体代码的运行，然后遇到yield停下来，
将yield后的值，当作本次调用的结果返回
'''
# g.__next__()

res1=g.__next__()
print(res1)
res2=g.__next__()
print(res2)
res3=g.__next__()
print(res3)

'''
小知识：关于a.__XXX__()的使用有个简单的办法
    XXX(a) 
'''


# 生成器的应用 写一下range的功能

# def my_range(start, stop, step):
#     print("start...")
#     while start < stop:
#         yield start
#         start += step
#     print("end...")


# g = my_range(1, 7, 2)  # 1，3，5
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))

# for n in my_range(1,8,1):
#     print(n)

'''
有了yield关键字，我们有了一种自定义的迭代器实现方式，Yield可以用于返回值，可以使一个函数暂停处于挂起状态
'''

