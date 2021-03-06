#로그인창 메소드
import dao
import bcrypt
#아이디와 비밀번호를 입력 후 테이블과 비교

def login(inform):
    id , pw = inform
    chkid = (id,)


    


    chkpw = dao.chkpwlogin(chkid)[0]
    if chkpw == 1: #애초에 아이디를 틀릴 경우
        print('아이디 또는 비밀번호가 틀렸습니다')#만약 아이디가 틀렸으면??
        return 1,1
    else :
        is_same = bcrypt.checkpw(pw.encode('utf-8'),chkpw.encode('utf-8')) #checkpw를 통해 입력한 pw와 db에 저장된 chkpw 해쉬 값을 비교함
        if is_same: #true 값이라면 로그인을 진행하고 닉네임을 리턴함
            value = (id,)
            chkedid,chkedname = dao.login(value)
            name = chkedname[0]
            
            return chkedid,name #아이디와 닉네임을 전달함
        else: #false면 실행됨
            print("아이디 또는 비밀번호가 틀렸습니다.") 
            return 1,1