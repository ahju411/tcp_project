import dao

def login(chkid):
    if dao.confrimid(chkid) == False:
        print("가입을 진행해도 좋습니다~")
        return True
    else:
        print('다른 아이디를 입력해주세요')
        return False