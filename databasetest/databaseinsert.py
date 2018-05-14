import pymysql

db = pymysql.connect("localhost","root","123456aa","mysql")

cursor = db.cursor()

#1.数据库插入操作
sql = """insert into employee(first_name,last_name,age,sex,income) 
          values('Tom','Tommy',20,'M',2000)"""

sql2 = """insert into employee(first_name,last_name,age,sex,income) 
          values('Fang','FangLijuan',18,'W',3000)"""

try:
    cursor.execute(sql)
    cursor.execute(sql2)
    db.commit()
except:
    print("发生了错误")
    #发生错误就回滚
    db.rollback()

db.close()
