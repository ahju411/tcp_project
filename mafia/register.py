
import dao
import bcrypt

#아이디 비번 이름 전화번호 순 

chkid = (input('아이디를 입력해주세요: '),)
while 1:
    if dao.confrimid(chkid) == False:
        print("가입을 진행해도 좋습니다~")
        break
    else:
        chkid = (input('다른 아이디를 입력해주세요: '),)
id = ''.join(chkid)
pw = (input('비밀번호를 입력해주세요: '))
encode_pw = bytes(pw,'utf-8')
hash_pw = bcrypt.hashpw(encode_pw,salt=bcrypt.gensalt())

name =input('이름을 입력해주세요: ')
phone = input('전화번호를 입력해주세요: ')
chknickname = (input('닉네임을 입력해주세요: '),)
while 1:
    if dao.confirmnickname(chknickname) == False:
        print('가입 되었습니다~')
        break
    else:
        chknickname = (input('다른 닉네임을 입력해주세요: '),)
nickname = ''.join(chknickname)
value = (id,hash_pw.decode('utf-8'),name,phone,nickname)

#dao.insert(value)
#dao.select()
dao.insert(value)






