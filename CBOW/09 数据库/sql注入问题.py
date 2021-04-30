import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='user_test',
    charset='utf8'  # 不要 utf-8
)


cursor=conn.cursor(pymysql.cursors.DictCursor)

username=input(">>>输入名字：").strip()
password=input(">>>输入密码：").strip()
'''注意引号的区别'''
# sql="select * from box where name='%s' and pwd='%s' " %(user,pwd)
sql="select * from box where name=%s and pwd=%s"

res=cursor.execute(sql,(username,password))
if res:
    print("登录成功")
else:
    print("登录失败")