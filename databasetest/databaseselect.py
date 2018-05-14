import pymysql

db = pymysql.connect("localhost","root","123456aa","mysql")
cursor = db.cursor()
sql = "select * from employee where income >= '%d'"%(1000)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print("-----------results:",results)
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print("fname={},lname={},age={},sex={},income={}".format(fname, lname, age, sex, income))
except:
    print("Error:unable to fetch data")

db.close()