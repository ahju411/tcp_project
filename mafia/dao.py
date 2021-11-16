import cx_Oracle
import os

#LOCATION = r"C:\instantclient_21_3"
#os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

#conn = cx_Oracle.connect("comet/1234@192.168.35.245:1521/XE")
#cursor = conn.cursor()
def makeDict(cursor): #sql실행된거 딕셔너리 만들기
    columnNames = [d[0] for d in cursor.description]

    def createRow(*args):
        return dict(zip(columnNames, args))
    
    return createRow

def select(): #정보 보여주기
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql = "select mem_id,mem_name, mem_phone,nickname from member"
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
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql = "insert into member values(:1,:2,:3,:4,:5)"
    cursor.execute(sql,t)
    conn.commit()
    cursor.close()
    conn.close()

def update(t): #닉넴 수정하기
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql = "update member set nickname=:1 where mem_id=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()

def delete(t): #탈퇴하기
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql ="delete from member where mem_id=:1 and mem_pw=:2"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()

def confrimid(id): #아이디 중복확인
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql ="select * from member where mem_id=:1"
    cursor.execute(sql,id)
    for i in cursor:
        if len(i) > 0:
            print("이미 사용중인 아이디입니다.")
            return True
    cursor.close()
    conn.close()
    return False

def confirmnickname(nickname): #닉네임 중복확인
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql ="select * from member where nickname=:1"
    cursor.execute(sql,nickname)
    for i in cursor:
        if len(i) > 0:
            print("닉네임이 사용중입니다.")
            return True
    cursor.close()
    conn.close()
    return False


def login(inform): #로그인 구현
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql ="select mem_name from member where mem_id=:1"
    #전달된 id 값 읽기
    id = inform[0]
    #pw = inform[1]
    cursor.execute(sql,inform)
    #cursor.rowfactory = makeDict(cursor)

    #sql 실행문이 있는지 확인하기 
    rows = (cursor.fetchall())
    if not rows :
        print('please register first')
        return False
    else:
        name = rows[0]
        return id,name
    cursor.close()
    conn.close()

def chkpwlogin(chkpw):
    conn = cx_Oracle.connect("comet/1234@118.217.168.174:1521/XE")
    cursor = conn.cursor()
    sql ="select mem_pw from member where mem_id=:1"
    #chkpw = pw[0]
    cursor.execute(sql,chkpw)
    #cursor.rowfactory = makeDict(cursor)

    #sql 실행문이 있는지 확인하기 
    rows = (cursor.fetchall())
    if not rows :
        print('아이디 또는 비밀번호가 틀렸습니다.')
        return False
    else:
        pw = rows[0]
        return pw
    cursor.close()
    conn.close()

    

