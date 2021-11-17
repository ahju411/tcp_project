import dao

def nickname(chknickname):
    if dao.confirmnickname(chknickname) == False:
        print('사용해도 좋습니다.')
        return True
    else:
        print('다른 닉네임을 입력해주세요')
        return False