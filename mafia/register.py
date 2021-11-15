import cx_Oracle
import os
import dao

#아이디 비번 이름 전화번호 순 

chkid = (input('아이디를 입력해주세요: '),)
while 1:
    if dao.confrimid(chkid) == False:
        print("가입을 진행해도 좋습니다~")
        break
    else:
        chkid = (input('아이디를 입력해주세요: '),)
id = ''.join(chkid)
pw = input('비밀번호를 입력해주세요: ')
name =input('이름을 입력해주세요: ')
phone = input('전화번호를 입력해주세요: ')
chknickname = (input('닉네임을 입력해주세요: '),)
while 1:
    if dao.confirmnickname(chknickname) == False:
        print('사용 가능한 닉네임입니다.')
        break
    else:
        chknickname = (input('닉네임을 입력해주세요: '),)
nickname = ''.join(chknickname)
value = (id,pw,name,phone,nickname)

#dao.insert(value)
#dao.select()
dao.insert(value)



