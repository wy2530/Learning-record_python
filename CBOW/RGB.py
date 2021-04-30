'''
图像处理：
    RGB
    数字图像本身是多维矩阵 ---三维
    高*宽*3
    单独提取通道
图像的深度：
    位 级 色
灰度图像：
    数组越大---像素越白
'''

# #导入模块
# from PIL import Image
# #打开图像
# img=Image.open(r"0497.bmp")
# img_new=img.crop((0,0,200,200))
# img_new.save("len2.png")

# #创建一个新的图像(模块，尺寸，大小)
# new=Image.new('L',img.size,255)
# width=img.size[0]
# heigth=img.size[1]
# #彩色图像转换为灰度图
# img=img.convert('L')

#画笔来画图
# Pen_size=3
# #扩散器
# Color_Diff=6

# for i in range(Pen_size+1,width - Pen_size-1):





# #图像组成
# img_mode=img.mode
# print(img_mode)
# #图像大小
# img_size=img.size
# print(img_size)
# #图像某一个坐标点的三原色
# img_get=img.getpixel((2,6))
# print(img_get)

# from skimage import io,data
# img=io.imread("123.png")
# io.imshow(img)

# import skimage.io as io
# from matplotlib import pyplot as plt
# img = io.imread('aa.png')
# io.imshow(img)
# plt.show() #添加此函数就能显示

# from skimage import data, io
# from matplotlib import pyplot as plt
# img = io.imread('aa.png')
# # 查看图片，使用io模块中的imshow方法
# io.imshow(img)
# # 保存图片
# plt.show()

# from skimage import io,data
# import matplotlib.pyplot as plt
# img=io.imread('123.png')
# plt.figure(num='astronaut',figsize=(8,8))  #创建一个名为astronaut的窗口,并设置大小
#
# plt.subplot(2,2,1)     #将窗口分为两行两列四个子图，则可显示四幅图片
# plt.title('origin image')   #第一幅图片标题
# plt.imshow(img)      #绘制第一幅图片
#
# plt.subplot(2,2,2)     #第二个子图
# plt.title('R channel')   #第二幅图片标题
# plt.imshow(img[:,:,0],plt.cm.gray)      #绘制第二幅图片,且为灰度图
# plt.axis('off')     #不显示坐标尺寸

# plt.subplot(2,2,3)     #第三个子图
# plt.title('G channel')   #第三幅图片标题
# plt.imshow(img[:,:,1],plt.cm.gray)      #绘制第三幅图片,且为灰度图
# plt.axis('off')     #不显示坐标尺寸
#
# plt.subplot(2,2,4)     #第四个子图
# plt.title('B channel')   #第四幅图片标题
# plt.imshow(img[:,:,2],plt.cm.gray)      #绘制第四幅图片,且为灰度图
# plt.axis('off')     #不显示坐标尺寸
#
# plt.show()   #显示窗口


import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值测试图像
img=color.rgb2gray("123.png")

#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

rows,cols=img.shape
ax1.axis([0,rows,cols,0])
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_title('contours')
plt.show()