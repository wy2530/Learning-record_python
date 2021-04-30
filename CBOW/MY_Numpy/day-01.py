import numpy as np
class Perceptron(object):
    '''
    eta:学习率
    n_iter:权重向量的训练次数
    w_:神经分叉权重向量
    errors_:用于记录神经元判断出错次数
    '''
    def __int__(self,eta=0.01,n_iter=10):
        self.eta=eta;
        self.n_iter=n_iter
        pass
    def fit(self,x,y):
        '''
        输入训练数据，培训神经元，x输入样本向量，y对应样本分类
        :param x: shape[n_samples,n_features]
                  [[1,2,3],[4,5,6]]
        :param y: n_samples:2
                  n_features:3

            y:[1,-1]
        """
        初始化权重向量0
        加一是因为前面算法提到的w0,也就是不调函数阈值
        """
        :return:
        '''

        self.w_=np.zero(1+x.sharpe[1])
        self.errors_=[]
        for _ in range(self.n_iter):
            errors=0
            '''
            X:[[1,2,3],[4,5,6]]
            y：[1,-1]
            zip(x,y)=[[1,2,3,1],[4,5,6,-1]]
            '''
            for xi,target in zip(x,y):
                '''
                update=n*(y-y')
                '''
                update=self.eta*(target-self.predict(xi))

                '''
                xi 是一个向量
                update * xi等价
                [ ▲w(1)=x[1]*update,▲w(2)=x[2]*update,▲w(2)=x[3]*uodate]
                '''
                self.w_[1:]+=update*xi
                self.w_[0] +=update

                errors+=int(update!=0.0)
                self.errprs_.append(errors)

                pass
            pass
        def net_input(self,x):
            '''
            z=w0*1+w1*x2+...wn*xn
            :param self:
            :param x:
            :return:
            '''
            return np.dot(x,self.w_[1:]+self.w_[0])
            pass
        def predict(self,x):
            return np.where(self.net_input(x)>=0.0,1.-1)
        pass


file="D:\day-01\iris.csv"
import pandas as pd
df=pd.read_csv(file,header=None)
df.head(10)