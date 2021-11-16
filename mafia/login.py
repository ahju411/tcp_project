import dao
import bcrypt
#아이디와 비밀번호를 입력 후 테이블과 비교

forchkpwID = (input('아이디를 입력해주세요: '),)
id = ''.join(forchkpwID) 
#if dao.confrimid(forchkpw) == False:
    #print('아이디 또는 비밀번호가 틀렸습니다')
pw = input('비밀번호를 입력해주세요: ')

# hash_pw = bcrypt.hashpw(encode_pw,salt=bcrypt.gensalt())
# print(hash_pw)
chkpw = dao.chkpwlogin(forchkpwID)[0]
if chkpw == 1:
    print('아이디 또는 비밀번호가 틀렸습니다')#만약 아이디가 틀렸으면??
    exit()
else :
    #print(chkpw)
    is_same = bcrypt.checkpw(pw.encode('utf-8'),chkpw.encode('utf-8'))
    if is_same:
        value = (id,)
        if dao.login(value) is False:
            print("뭘봐")
        else :
            chkedid,chkedname = dao.login(value)
            name = chkedname[0]
            print('당신의 닉네임은: ',name)
    else:
        print("아이디 또는 비밀번호가 틀렸습니다.")