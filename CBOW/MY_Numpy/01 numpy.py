# import numpy as np
'''
np 矩阵
'''

'''
属性
'''
# array=np.array([[1,2,3],
#                [2,3,4]])
# #属性
# print(array)
# #维度
# print('number of dim:',array.ndim)
# #形状(行，列)
# print('sharp:',array.shape)
# #size 个数
# print('size',array.size)

'''
创建array
'''
import numpy as np

'''一维'''

# a=np.array([2,3,4],dtype=np.int64)
# print(a)
# print(a.dtype)

'''二维'''
# array=np.array([[1,2,3],
#                [2,3,4]])

'''全要0的矩阵(行列'''
a=np.zeros((3,4))
print(a)

'''全要1的矩阵（2* 全是2）'''
a2=2*np.ones((3,4))
print(a2)

'''什么都没有的矩阵//随机'''
a3=np.empty((4,5))
print(a3)

'''有序数列或矩阵(前闭后开)'''
a4=np.arange(12,20,2)
print(a4)

'''有序数列或矩阵(前闭后开)  4*4=12'''
a4=np.arange(16).reshape((4,4))
print(a4)
'''生成线段：（从哪，到哪，步长）.resharp(n,m) 要求n*m=步长'''
a5=np.linspace(1,10,6).reshape((2,3))
print(a5)
'''arange减/加/乘法'''
a=np.arange(10,30,5)
b=np.array([1,2,3,4])
print('a-b',a-b)
print(a+b)
print(a**2) #(a的平方)
'''三角函数'''
d=100*np.cos(a) #给a求cos值，并乘10
print(d)
''''''
print(a<20)

'''
矩阵乘法
1、逐个相乘
2、矩阵乘法
注意维度
'''
a=np.arange(4).reshape(2,2)
b=np.array([[2,3],
           [4,5]])
print(a)
print(b)
print(a*b)
#c c_2方式一样
c=np.dot(a,b)
c_2=a.dot(b)

print(c)
print(c_2)
print("====>")
'''随机'''
a=np.random.random((2,4))
print(a)
print(np.sum(a))
'''
axis表示维度，
0表示列，每一个列的最小值
1表示行，每一个行的最小值
'''
print(np.min(a,axis=0))
print(np.max(a))

'''
索引最大/小位置、平均值、中位数
'''
A=np.arange(0,20).reshape(4,5)
print(A)
print(np.argmax(A))
print(np.argmin(A))
#平均值的不同表示方式
print(np.mean(A))
print(A.mean())
print(np.average(A))
#中位数
print(np.median(A))
#累加返回列表
print(np.cumsum(A))
#累差还是矩阵(会少一列哦~)
print(np.diff(A))

#循环输出每一行
A=np.arange(3,15).reshape((3,4))
print(A)
#循环输出每一行
for row in A:
    print(row)
#循环输出每一列(必须要转置)
for column in A.T:
    print(column)

# 将矩阵整成一个列表
print(A.flatten())
#循环输出每一项
for item in A.flat:
    print(item)

#合并

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
#AB上下合并合并
C=np.vstack((A,B))
print(A.shape,C.shape)
print(C)
#AB上下合并合并
C=np.hstack((A,B))

#将A写成[[1],[1],[1]].T的形式
#print(A[np.newaxis,:].shape)

print("====")
#多个合并,并且可以指定维度的个数
print(np.concatenate((A,B,A,B),axis=1))


#分割
A=np.arange(12).reshape((3,4))
print(A)
#均分
print(np.split(A,2,axis=1))
#不等分军阀
print(np.array_split(A,3))

#
# np.vsplit((A,1))
# np.hsplit((A,1))

#深浅copy(一起变，浅copy)(不关联,deep.copy)
b=np.arange(4)
a=b
print(b)
print(a)
print(a is b)
c=b.copy()
print(c)
print(c is b)

'''
pandas  类似于字典的排序
'''
import pandas as pd

s=pd.Series([1,3,6,np.nan,44,1])
#自动 加字典和dtype
print(s)

dates=pd.date_range('20200601',periods=6)
print(dates)

'''
DataFrame转化为了列表形式，np.XX是数据来源，index=按某种方式索引，列名称
默认索引于行数都是0 1 2 ...
'''
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['第一列','第2列','第3列','第4列'])
print(df)
#每一列的类型
print(df.dtypes)
#打印单独DataFrame的行名、列名、值、
print(df.columns)
print(df.index)
print(df.values)
#描述 计数、平均值、标准值、最小值、最大值、会忽略不可计算的数
print(df.describe())

#行列翻转
print(df.T)
#根据行列排序 axis=按行或按列，ascending=正序或倒序
dfA=df.sort_index(axis=0,ascending=False)
##根据行值排序(从小到大排序)
dfB=df.sort_values(by='第2列')
print(dfA)
print(dfB)

print("============")
#选择数据
print(df.第一列)
print("============")
print(df['第一列'])

print(df[0:2])
print(df['20200603':'20200604'])

#高级数据选择,1、根据标签选择(类似)
print("===")
print(df.loc['20200602'])
#打印某行某列
print(df.loc['20200603',["第2列",]])


#2、根据位置选择df.iloc[第几行,第几位]
print("my list")
print(df)
print("iloc=======")
print(df.iloc[3])
print("iloc=======")
print(df.iloc[3,0])
#[第几行：到第几行,第几列：第几列]
print(df.iloc[1:3,2:])
print("iloc=======")

#3、条件选择
print(df[df['第一列']>0])

#设置值，可以选出来后直接赋值

#加一个为NaN的序列np.nan

'''
如何处理消失了的数据
1、丢掉缺失的数据dropna()
axis=选择丢掉的是行还是列，
how=选择丢掉的方式，任何一个是空值，还是所有数据都是空值
2、用0来填充
fillna() 用0来填补空缺值
3、检查是否有丢失的数据
isnull() 返回的是布尔值，没有值返回True
np.any() 有任何缺失便返回True
'''
print(df.dropna(axis=0,how='any')) #{'any','all'}
print(df.fillna(value=0))
print(np.any(df.isnull())==True)

'''
导入文件
read_csv
read_pickle
read_json
...
导出文件
to_csv
to_pickle
to_json
...

pd.read_csv(r"文件名.后缀名")
pd.to_csv(r"新文件名.后缀名")
'''

'''
合并多个DataFrame #concatenating
1、同列合并(列名相同)，(注意方向 axis 调方向)
concat([需要合并的表格，注意在列表中]，axis=确定合并方向，ignore_index=是否忽略原来的索引)
2、行名，列名不同：join['inner','outer']
join='outer'默认类型，全连接，没有的补NaN
Join='inner'只取相同部分
concat([list],join='XXX',ignore_index='',axis='')
'''
# df_1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df_2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df_3=pd.DataFrame(np.ones((3,4))*3,columns=['a','b','c','d'])
#
# res=pd.concat([df_1,df_2,df_3],axis=0,ignore_index=True)
# print(res)

#join['inner','outer']
df_1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=['1','2','3'])
df_2=pd.DataFrame(np.ones((3,4))*1,columns=['e','b','c','d'],index=['2','3','4'])

res=pd.concat([df_1,df_2],join='inner',ignore_index=True,axis=0)
print(res)
print("===="
      "====="
      "=====")
#横向合并，索引没有时补NaN没有 join_axes=[df_1.index](可能已经被弃用了)
res2=pd.concat([df_1,df_2],axis=1)
print(res2)

#append
df_A=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df_B=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df_C=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
#默认纵向添加（填一个不用列表，填多个用列表）
res4=df_A.append([df_B,df_C],ignore_index=True)
print(res4)

# 只需要添加一行/一列 Series
df_A=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df_A.append(s1,ignore_index=True)
print(res)

'''
merge
pd.merge(A,B,on=基于哪一个columns进行合并)
连接，默认连接方式how='inner'
how=['inner','outer','left','right']
indicator=True : 显示数据格式
indicator='XXX': 改名字

suffixes=['XXX','XXX'] #添加后缀名
'''
pd.merge(A,B,on=['C','D'])
#pd.merge(left,right,right_index=,left_index=)



