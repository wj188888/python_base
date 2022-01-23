# -- coding:utf-8 --
import pymysql

# 获取连接
conn = pymysql.connect(
    host='127.0.0.1',
    user = 'root',
    passwd = '123456',
    db='mysql',
    port = '3306',
    charset = 'utf8'
)
# 获取数据
cursor = conn.cursor()
cursor.excute('use user')
cursor.excute('select * from user')
res = cursor.fetchone()
print(res)
cursor.close()
conn.close()