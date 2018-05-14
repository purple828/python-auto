import pymysql

db = pymysql.connect("localhost","root","123456aa","mysql")
cursor = db.cursor()
sql = "delete from employee where age> {}".format(20)
try:
    cursor.execute(sql)
    db.commit()
except:
    print("delete Error")
    db.rollback()

db.close()