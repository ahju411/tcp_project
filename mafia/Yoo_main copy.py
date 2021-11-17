
import time
import threading
import random
from threading import *

i=0
killResult=""
arrestResult=""

class SET_USER_JOB:
    def __init__(self,nickname,job) :
        self.nickname = nickname
        if job == 1 :
            self.job = "마피아1"
        if job == 2 :
            self.job = "마피아2"
        if job == 3 :
            self.job = "경찰"
        if job == 4 :
            self.job = "의사"
        if job == 5 :
            self.job = "시민1"
        if job == 6 :
            self.job = "시민2"
        if job == 7 :
            self.job = "시민3"
        if job == 8 :
            self.job = "시민4"


def startTimer():
    global i
    print(i)
    i-=1
    timer = threading.Timer(1,startTimer)
    timer.start()
    if i==0 :
        timer.cancel()
        return i
    




####### main()


mafia_su=2
citizen_su=4

## 직업 랜덤부여  
# 들어온 유저들을 받았다고 가정시
user = ["철철철철철철","뭘까이기분은","김민꾜우","감스트입니다"
,"페이커","hide on bush","skt t1 faker","쇼메이커"]


joblist = [1,2,3,4,5,6,7,8]  
joblist = random.sample(joblist,8) # joblist 숫자 랜덤으로 섞기

# 섞은번호랑 유저별로 합체~
user1 = SET_USER_JOB(user[0],joblist[0])
user2 = SET_USER_JOB(user[1],joblist[1])
user3 = SET_USER_JOB(user[2],joblist[2])
user4 = SET_USER_JOB(user[3],joblist[3])
user5 = SET_USER_JOB(user[4],joblist[4])
user6 = SET_USER_JOB(user[5],joblist[5])
user7 = SET_USER_JOB(user[6],joblist[6])
user8 = SET_USER_JOB(user[7],joblist[7])

usersetlist = [user1.nickname,user2.nickname,user3.nickname,user4.nickname,user5.nickname,user6.nickname,user7.nickname,user8.nickname]
userjobsetlist = [user1.job,user2.job,user3,user4.job,user5.job,user6.job,user7.job,user8.job]

inputusername = input("당신의 닉네임은? :")


while(i<8):

    if usersetlist[i] == inputusername:
        print("당신 직업은 : " , userjobsetlist[i] )
        myname = usersetlist[i]
        myjob = userjobsetlist[i]
        break

    i=i+1




while(1):
    th1=Thread(target=startTimer)
    i=5
    print("밤 입니다.")
    th1.start()
    time.sleep(8)

    th2=Thread(target=startTimer)
    i=5
    print("아침 입니다.")
    th2.start()
    time.sleep(8)



if(mafia_su==0):
    print("시민팀 승리")

elif mafia_su==citizen_su:
    print("마피아팀 승리")





###############################

