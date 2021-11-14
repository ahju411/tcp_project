import oracleprac as dao

name = input('이름을 입력하세요')
id = input('아이디를 입력하세요:')
pw = input('비밀번호를 입력하세요')

t=(name,id,pw)

dao.insert(t)
dao.select()