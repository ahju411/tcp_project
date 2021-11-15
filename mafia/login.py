import cx_Oracle
import os
import dao

#아이디와 비밀번호를 입력 후 테이블과 비교

id = input('아이디를 입력해주세요')
pw = input('비밀번호를 입력해주세요')
value = (id,pw)
#chkedid,chkedpw = dao.login(value)
#f (dao.login(value)) is not False:
if dao.login(value) is False:
    print("뭘봐")
else :
    chkedid,chkedname = dao.login(value)
    name = chkedname[0]
    print(name)
   # print('hi')