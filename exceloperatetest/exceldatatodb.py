'''
读取excel文件内容并写入数据库

'''
from openpyxl import load_workbook
import pymysql

conn = pymysql.connect("localhost","root","123456aa")

conn.autocommit(1)

cur = conn.cursor()

#创建数据库exceltest
name="exceltest"
db_sql = "create database if not exists %s"%name
cur.execute(db_sql)

conn.select_db(name)

