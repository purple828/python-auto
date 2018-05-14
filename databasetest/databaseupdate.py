import pymysql

db = pymysql.connect("localhost","root","123456aa","mysql")
cursor = db.cursor()

sql = "update employee set age=age+1 where sex='{}'".format('W')

try:
    cursor.execute(sql)
    db.commit()
except:
    print("update Error")
    db.rollback()

db.close()