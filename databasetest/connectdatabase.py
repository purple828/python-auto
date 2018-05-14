import pymysql

#打开数据库
db = pymysql.connect("localhost","root","123456aa","mysql")

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# #使用execute()方法执行SQL查询
# cursor.execute("SELECT VERSION()")
# #使用fetchone()方法获取单条数据
# data = cursor.fetchone()
# print("Database version:%s"%data)

cursor.execute("drop table if exists employee")

sql= """create table employee(
    first_name varchar(20) not NULL ,
    last_name varchar(20) ,
    age int,
    sex varchar(1),
    income DECIMAL )  """

cursor.execute(sql)

#关闭数据库
db.close()
