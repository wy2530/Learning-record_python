
def auth(db_type):
    def outter(func):
        def wapper(*args,**kwargs):
            # print("开始")
            if db_type=="file":
                print("1")
                res = func(*args, **kwargs)
                return res
            elif db_type == "mysql":
                print("2")
                res = func(*args, **kwargs)
                return res
            else:
                print("不可认证")
                # print("不可认证")
        return wapper
    return outter

@auth(db_type="file")
def index():
    print("222")

index()