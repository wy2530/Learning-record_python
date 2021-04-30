# with open('first.txt',mode='wt',encoding="utf-8") as f:
#     f.write("你好，我是第一个文件，我要开始复制了")

# with open('first.txt',mode='rt',encoding='utf-8')as f1,\
#      open('two.txt',mode='wt',encoding='utf-8') as f2:
#     for line in f1:
#         f2.write(line)



# 1、拷贝工具：
old_file=input("请输入需要的路径：")
new_file=input("请输入新文件路径：")
with open(r'{}'.format(old_file),mode='rt',encoding='utf-8')  as f1,\
    open(r'{}'.format(new_file),mode='wt',encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)







