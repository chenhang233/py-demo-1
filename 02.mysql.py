
import pymysql
from pymysql.cursors import DictCursor


conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db1',charset='utf8')
cur = conn.cursor(DictCursor)

sql = "SELECT * FROM stu"

cur.execute(sql)

res = cur.fetchall()

print(res)

conn.close()