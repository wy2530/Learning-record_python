class Myclass(object):
    def func1(self):
        print('func1')
        return self

    def func2(self):
        print('func1')
        return self


obj = Myclass()
obj.func1().func2()