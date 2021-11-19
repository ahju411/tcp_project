#회원가입 닉네임 중복 확인 메소드
import dao

def nickname(chknickname):
    if dao.confirmnickname(chknickname) == False:
       
        return True
    else:
        
        return False