import cx_Oracle
import os

# LOCATION = r"C:\instantclient_21_3"
# os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

#conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
#cursor = conn.cursor()

def select(): #정보 보여주기
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "select mem_id,mem_name, mem_phone, from member"
    cursor.execute(sql)

    for row in cursor:
        for i in range(len(row)):
            if i ==3:
                description=row[3].read()
            print(row[i], end = " ")
        print()
    cursor.close()
    conn.close()

def insert(t): #회원 가입하기
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "insert into member values(:1,:2,:3,:4)"
    cursor.execute(sql,t)
    conn.commit()
    cursor.close()
    conn.close()

def update(t): #정보 수정하기
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql = "update member set name=:1 where id=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()

def delete(t): #탈퇴하기
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql ="delete from member where mem_id=:1 mem_pw=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()

def confrimid(id):
    conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
    cursor = conn.cursor()
    sql ="select * from member where mem_id=:1"
    check = cursor.execute(sql,id)
    for i in cursor:
        if len(i) > 0:
            print("존재합니다")
            return True
    cursor.close()
    conn.close()
    return False