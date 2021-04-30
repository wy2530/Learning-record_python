import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data
#Series
# data=pd.Series(np.random.randn(1000),index=np.arange(1000))
# #累加
# data=data.cumsum()
# data.plot()
# # plt.plot(x=,y=)
# plt.show()

#
data=pd.DataFrame(np.random.randn(1000,4),
             index=np.arange(1000),
             columns=list('ABCD'))
data=data.cumsum()
#输出前5个数据
# print(data.head(5))
#画图
# data.plot()
# plt.show()


'''
画图的方法：
'bar','hist','box','kde','area','scatter','hexbin','pie'
'''

ax=data.plot.scatter(x='A',y='B',color='red',label='Class1')
data.plot.scatter(x='B',y='C',color='green',label='Class2',ax=ax)
plt.show()