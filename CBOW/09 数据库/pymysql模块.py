import pymysql

# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='user_test',
    charset='utf8'  # 不要 utf-8
)

# 产生一个游标对象，类似于在终端输入mysql -u root -p
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from epm;'

# execute返回的行数是当前语句可影响的行数
res = cursor.execute(sql)
print(res)

# 获取命令的执行结果
# 链接时不加参数，fetchone元组返回，只有一条
# 链接时可以加参数
print(cursor.fetchone())  # 只有一条
print(cursor.fetchall())  # 拿所有的

# cursor.scroll(1, 'relative')
# cursor.scroll(2, 'absolute')
print(cursor.fetchmany(5))

'''
如果直接连着取取每次，你会发现数据有移动
因为这个取数据类似于光标移动，你取一个，光标后移动一个

可以自己设置光标移动  
cursor.scroll(1, 'relative')   #相对移动
cursor.scroll(2, 'absolute')   #绝对移动
'''
