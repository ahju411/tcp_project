import cx_Oracle
import os

LOCATION = r"C:\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

connectection = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
sql = 'select * from test_db'
cursor = connectection.cursor()
cursor.execute(sql)


 
for name in cursor:
    print("이름:",name)