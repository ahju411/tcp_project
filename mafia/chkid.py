#회원가입 아이디 확인 메소드
import dao

def login(chkid):
    if dao.confrimid(chkid) == False:
        
        return True
    else:
        
        return False