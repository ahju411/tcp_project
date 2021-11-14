import cx_Oracle
import os

# LOCATION = r"C:\instantclient_21_3"
# os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

#conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
#cursor = conn.cursor()

def select():
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "select name,id from test_db"
    cursor.execute(sql)

    for row in cursor:
        for i in range(len(row)):
            if i ==3:
                description=row[3].read()
            print(row[i], end = " ")
        print()
    cursor.close()
    conn.close()

def insert(t):
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "insert into test_db values(:1,:2,:3)"
    cursor.execute(sql,t)
    conn.commit()
    cursor.close()
    conn.close()

def update(t):
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "update test_db set name=:1 where id=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()

def delete(t):
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql ="delete from test_db where id=:1 password=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()
