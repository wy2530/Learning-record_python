# 1、通用文件copy工具实现（包含图片、视频等）
"""
知识补充：
os.path: 模块主要用于获取文件的属性。
os.path.exists: 如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
os.path.isfile(path): 判断路径是否为文件

注意：是文件而不是文件夹，如果写出文件夹 exists：会报错，isfile会说文件不存在
"""
import os
while True:
    old_file=input("请输入文件路径：").strip()
    if not os.path.exists(old_file):
        print("源文件路径不存在，请重新输入！")
        continue
    else:
        new_file=input("新文件路径：").strip()

        with open('{}'.format(old_file),'rb') as r_f,\
            open('{}'.format(new_file),'wb') as w_f:
            for line in r_f:
                w_f.write(line)
    break


