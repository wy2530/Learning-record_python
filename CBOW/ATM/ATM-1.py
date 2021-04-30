"""
1、注册功能
2、登录功能
3、充值功能
4、转账功能
5、提现功能
"""


# 1、注册功能

def register():
    username = input("your name:").strip()
    with open('register.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            name = line.strip().split(":")[0]
            if name == username:
                print("用户名已存在！请重新输入")
                register()
                break  # 将register执行完后,跳出循环
        else:
            while True:
                password = input("your password:").strip()
                re_password = input("your password again:").strip()
                with open('register.txt', mode='at', encoding='utf-8') as f2:
                    if password == re_password:
                        f2.write("\n{}:{}".format(username, password))
                        print("注册成功!")
                        break
                    else:
                        print("密码不一致，请重新输入！")
                print("登录输入Y，不登录输入N")
                is_login = input("是否选择登录：")
                if is_login == 'Y':
                    login()
                elif is_login == 'N':
                    print("正在退出...")


# register()


# 2)登录功能

def login():
    usename = input("your usename:").strip()
    password = input("your password:").strip()
    with open('register.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            name, pwd = line.strip().split(":")
            if usename == name and pwd == password:
                print("登录成功")
                break
        else:
            print("用户名或密码错误！请重新登录")


# login()
register()


# 3)充值功能

def pay_money(username):
    '''
    :param username: 需要充值的用户
    :return:
    '''
    # 1、读取用户数据，放入字典
    dic = {}
    with open('db.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(":")
            dic[user] = float(money)
    # 2、判断是否存在，不存在直接退出
    if username not in dic:
        print('用户不存在,结束程序！')
        return
    # 3、循环让用户充值
    while True:
        money = input('请输入充值金额:').strip()
        # money.isdigit()用来判断字符串是否全有数字组成

        if not isinstance(money, float):  # if not money.isdigit()用来判断是否是整型数
            print('请输入数字！')
            continue
        # 改金额
        money = float(money)
        dic[username] += money
        # 写入文件
        with open("db.txt", mode='wt', encoding='utf-8') as f:
            for user, money in dic.items():
                f.write(f'{user}:{money}\n')
            print("充值成功")
        break


# pay_money('liming')

# a=15.5
# print(isinstance (a,float))

'''
注册和登录功能：
    注册功能：不加######包含的代码，单独调用register()没问题
    登录功能：单独调用login()没问题

    我想加个功能，就是注册之后可以直接登录，就是######里的那一段
    我再调用register()时，出现了错误(有图片)

    我尝试了顺序问题导致的错误，把login放在了 register()上面，出现的问题是一样的  
    
错误原因:在文件还没有关闭时就又一次读入了，
           再文件没有关闭时，写入的东西都保存在内存中，还没有写入到硬盘，是读不出来的
    
充值问题：
    一开始写的是if not money.isdigit()用来判断是否全是数字
    写整数 运行结果完全没有问题
    
    后来认为金额有小数，尝试了如何判断是否是浮点数
    找到另一个函数
    
    isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    疑惑：
       a=15.5
       print(isinstance (a,float)) 
       测试结果为True
       
      那下面这一段程序就是：
        if True:
            print('请输入数字！')
        应该会执行而输出'请输入数字！，
        但是运行结果是'充值成功'？？？
'''


# 4)转账功能
def transfer(A_user, B_user, transfer_money):
    '''
    :param A_user: 转账的人
    :param B_user: 收钱的人
    :param transfer_money: 转款金额
    :return:
    '''

    # 1、读取用户A剩多少钱
    dic = {}
    with open('db.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(":")
            # 需要进行强制转化，不然str类型与float类型无法只接相加
            dic[user] = float(money)
        print(dic)
        '''
        dic.get(A_user):
            如果使用get,用户不存在时返回None
            if not None：
                执行语句

        小问题：如果用户金额是0
            if not 0：
                仍然会执行此程序

        优化:直接判断用户是否存在字典内就好
        '''
        if A_user not in dic:
            # if  not dic.get(A_user):
            print("没有此用户！")
            return
        if B_user not in dic:
            print("没有此用户！")
            return
        print('转账前：', dic)

        # dic.get可以直接得到与key匹配的value
        if dic.get(A_user) >= transfer_money:
            # A减钱
            dic[A_user] -= transfer_money
            # B加钱
            dic[B_user] += transfer_money
            #
            print('转账后：', dic)

            with open('db.txt', mode='wt', encoding='utf-8') as f:
                for user, money in dic.items():
                    f.write(f'{user}:{money}\n')
        else:
            print("余额不足,请充值")


# transfer('tank','liming',5000)


# 5)提现功能：用户提现，余额减少即可
def withdraw(get_user, get_money):
    """
    :param get_user: 提现的用户
    :param get_money: 提现的钱
    :return:
    """
    dic = {}
    with open('db.txt', mode="rt", encoding='utf-8') as f:
        for line in f:
            user, money = line.strip().split(':')
            dic[user] = float(money)

        print(dic)
        if get_user not in dic:
            print("该用户不存在")

        if get_money <= dic.get(get_user):
            dic[get_user] -= get_money
            print(dic)

            with open('db.txt', mode='wt', encoding='utf-8') as f:
                for user, money in dic.items():
                    f.write(f'{user}:{money}\n')
            print("提现成功")
        else:
            print("余额不足，无法提现")

# withdraw('wy',50)
