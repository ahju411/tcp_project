import bcrypt

bytes_password = b"this is password"
bytes_hashed_password = bcrypt.hashpw(password=bytes_password, salt=bcrypt.gensalt())
print("해시 값:", bytes_hashed_password)

bytes_password2 = b"this is passwor"
is_same = bcrypt.checkpw(bytes_password2,bytes_hashed_password)
print('일치 불일치:',is_same)

pw = (input('비밀번호를 입력해주세요: '))
encodepw = bytes(pw,'utf-8')
print(encodepw)