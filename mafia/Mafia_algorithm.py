
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


## 직업 랜덤부여  
# 들어온 유저들을 순서대로받았다고 가정시
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

'''
inputusername = input("당신의 닉네임은? :")


while(i<8):

    if usersetlist[i] == inputusername:
        print("당신 직업은 : " , userjobsetlist[i] )
        myname = usersetlist[i]
        myjob = userjobsetlist[i]
        break

    i=i+1

'''
# 게임 초기세팅
mafia_su = 2
citizen_su = 6



## 9는 마피아였던 사람이 죽은상태로 나타냄, 10은 그냥 나머지 직업이 죽은상태
## 이 while(1) 타이머 주기로 밤 > 아침 > 투표시간 >반론 > 최후의투표 반복할거임.
while(1): 
    ############################## 임시 초기데이터 베이스 설정, 
    user1 = SET_USER_JOB("A",1)
    user2 = SET_USER_JOB("B",2)
    user3 = SET_USER_JOB("C",3)
    user4 = SET_USER_JOB("D",4)
    user5 = SET_USER_JOB("E",5)
    user6 = SET_USER_JOB("F",6)
    user7 = SET_USER_JOB("G",7)
    user8 = SET_USER_JOB("H",8)
    usersetlist = [user1.nickname,user2.nickname,user3.nickname,user4.nickname,user5.nickname,user6.nickname,user7.nickname,user8.nickname]
    userjobsetlist = [user1.job,user2.job,user3,user4.job,user5.job,user6.job,user7.job,user8.job]

    ###############
    # 밤에 가능한 모든 경우의수 테스트..
    myjob=""
    mafia_su=2
    kill_1_user="A"
    kill_2_user="A"
    arrest_user=""
    heal_user="B"
    ##
    th1=Thread(target=startTimer) 
    i=3
    print("밤 입니다.")
    th1.start()
    if myjob=="마피아1" :
        kill_1_user=input("마피아1 죽일 사람을 선택하세요. : ")
    elif myjob=="마피아2":
        kill_2_user=input("마피아2 죽일 사람을 선택하세요. : ")
    elif myjob=="경찰":
        arrest_user=input("정체를 알고싶은 사람을 선택하세요. : ")
        p=0
        for k in usersetlist:
            if k == arrest_user:
                print(k,"는(은) ",userjobsetlist[p]," 입니다. ")
            else:
                p=p+1
        
    elif myjob=="의사":
        heal_user=input("마피아의 공격으로부터 치료하고 싶은 선택하세요.:")


    time.sleep(5) #    ↑ 밤동안 각자 직업들 열일하기             ↓ 각자 작업들 결과 종합 및 출력하기
    
  
    if mafia_su==2: # 마피아 둘 생존시 
        if kill_1_user == kill_2_user: # 마피아 둘이서 똑같은놈 지목해야 살해가능함
            if kill_1_user != heal_user:
                p=0
                for i in usersetlist:
                    if i == kill_1_user:
                        print(kill_1_user,"는(은) 밤에 살해당했습니다.")
                        usersetlist[p]="시체"
                        if userjobsetlist[p] == "마피아1" or userjobsetlist[p] == "마피아2":
                            usersetlist[p]="마피아죽음"
                            mafia_su-=1
                        else:
                            citizen_su-=1
                    else:
                        p+=1
             
            elif kill_1_user == heal_user:
                print("누군가가 마피아의 공격으로부터 살아남았습니다.")
        
        else:
            print("밤에 아무런 일이 없었습니다.")
    

    elif mafia_su==1: # 마피아 한명 생존시 코드 짧게할수있을거같은데  빡대가리라 못하겠내
       
        mafia_live_flag=0
        for k in userjobsetlist:
            if k == "마피아1":
                mafia_live_flag=1
            elif k == "마피아2":
                mafia_live_flag=2
        
        

        if mafia_live_flag==1: # 마피아1 생존시
            p=0
            for m in usersetlist:
                if m==kill_1_user:
                    if m!=heal_user:
                        print(kill_1_user,"는(은) 밤에 살해당했습니다.")
                        usersetlist[p]="시체"
                        userjobsetlist[p]="시민죽음"
                        citizen_su-=1
                    elif m==heal_user:
                        print("누군가가 마피아의 공격으로부터 살아남았습니다.")
                else:
                    p=p+1

        elif mafia_live_flag==2: # 마피아2 생존시
            p=0
            for m in usersetlist:
                if m==kill_2_user:
                    if m!=heal_user:
                        print(kill_2_user,"는(은) 밤에 살해당했습니다.")
                        usersetlist[p]="시체"
                        userjobsetlist[p]="시민죽음"
                        citizen_su-=1
                    elif m==heal_user:
                        print("누군가가 마피아의 공격으로부터 살아남았습니다.")
                else:
                    p=p+1            

  
    
    time.sleep(1)
    

    th2=Thread(target=startTimer)
    i=5
    print("아침 입니다.")
    th2.start()
    time.sleep(8)

    th3=Thread(target=startTimer)
    i=5
    print("투표시간 입니다.")
    th3.start()
    time.sleep(8)

    th4=Thread(target=startTimer)
    i=5
    print("최후의 반론 입니다.")
    th4.start()
    time.sleep(8)

    th5=Thread(target=startTimer)
    i=5
    print("최후의 투표 입니다.")
    th5.start()
    time.sleep(8)



if(mafia_su==0):
    print("시민팀 승리")

elif mafia_su==citizen_su:
    print("마피아팀 승리")





###############################

