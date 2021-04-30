import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='user_test',
    charset='utf8'  # 不要 utf-8
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

# 调用存储过程
cursor.callproc('p1', (1, 5, 10))
print(cursor.fetchall())

cursor.execute('select @_p1_2;')
print(cursor.fetchall())
