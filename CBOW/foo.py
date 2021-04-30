print('模块foo==>')

x=1

def get():
    print(x)

def change():
    global  x
    x=0

print(__name__) #每一个py文件都内置的属性,结果为__main__
'''
1、当该文件被当成程序直接运行时，__name__的值为'__main__'
2、当该文件被当成模块导入时，__name__的值为该文件的名字
'''
if __name__=='__main__':
    print("被当成执行程序")
else:
    print("被当成模块导入")

'''
小知识：
    直接写main，python会自动补全if __name__=='__main__':
'''

__all__=['x','get','change']