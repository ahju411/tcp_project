import dao
import bcrypt
#아이디와 비밀번호를 입력 후 테이블과 비교

forchkpw = (input('아이디를 입력해주세요'),)
id = ''.join(forchkpw)
pw = input('비밀번호를 입력해주세요')

# hash_pw = bcrypt.hashpw(encode_pw,salt=bcrypt.gensalt())
# print(hash_pw)
chkpw = ''.join(dao.chkpwlogin(forchkpw))
print(chkpw)
is_same = bcrypt.checkpw(pw.encode('utf-8'),chkpw.encode('utf-8'))
if is_same:
    value = (id,)
    #chkedid,chkedpw = dao.login(value)
    #f (dao.login(value)) is not False:
    if dao.login(value) is False:
        print("뭘봐")
    else :
        chkedid,chkedname = dao.login(value)
        name = chkedname[0]
        print(name)
    # print('hi')
else:
    print("아이디 또는 비밀번호가 틀렸습니다.")