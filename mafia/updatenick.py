import cx_Oracle
import os
import dao

#닉네임 변경하기 이미 로그인 된 상태가 가정했으니 아이디는 틀리면 안됨

id = input('아이디를 입력해주세요: ')
chknickname = (input('닉네임을 입력해주세요: '),)
while 1:
    if dao.confirmnickname(chknickname) == False:
        print('닉네임이 변경되었습니다.')
        break
    else:
        chknickname = (input('다른 닉네임을 입력해주세요: '),)
nickname = ''.join(chknickname)
value = (nickname,id)

#dao.insert(value)
#dao.select()
dao.update(value)
