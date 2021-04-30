# import os #用于与操作系统交互的模块
# #1、通用文件copy工具实现
# while True:
#     #1) 接收用户需要拷贝的源文件
#     source_file=input("请输入源文件路径：").strip()
#     #2)判断源文件是否存在
#     print(os.path.exists(source_file))
#     #os.path.exists----》(如果文件存在，返回True)
#     if not os.path.exists(source_file):
#         print('当前文件路径不存在，请重新输入：')
#         continue
#     #3)让用户输入拷贝后的文件路径
#     dst_file=input('请输入copy后的文件路径：').strip()
#     with open("{}".format(source_file),mode='rb') as f1,\
#         open("{}".format(dst_file),mode='wb') as f2:
#         #w,a均可,一个写，一个追加
#         for line in f1:
#             f2.write(line)
#     break #记得退出功能


# dic={'a':"1",'b':"2",'c':3}
# print(dic.get('a'),type(dic.get('a')))
# dic['a']


x = 10
l = ['a', 'b', x]
print("一开始的x===》id",id(x))
print("一开始的l[2]===》id",id(l[2]))
x = 123
print("后来的x===》id",id(x))
print("l[2]===》id",id(l[2]))

l[2]=12
print(l[2])
print("l[2]===》id",id(l[2]))
print(x)

