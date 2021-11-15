import cx_Oracle
import os
import dao

#아이디 비번 이름 전화번호 순 

chkid = (input('아이디를 입력해주세요: '),)
id = ''.join(chkid)
if dao.confrimid(chkid) == False:
    print("가입을 진행해도 좋습니다~")
else:
    exit()
pw = input('비밀번호를 입력해주세요: ')
name =input('이름을 입력해주세요: ')
phone = input('전화번호를 입력해주세요: ')
value = (id,pw,name,phone)

#dao.insert(value)
#dao.select()
dao.insert(value)



