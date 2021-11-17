
import time
import threading
import random

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


def timer(sec,myjob):
    temp=sec
    global gamemode


    if temp == 60 :
        print("밤입니다. ")
        i=0
        if myjob == 1 or myjob == 2 : ## 마피아 능력
            kill = input("죽일사람 선택하세요")
            while(i<8):
                if kill == i:
                    print("지목한사람 : ", kill )
                    killResult = i
                    break
            
        
        
        elif myjob == 3: ## 경찰 능력
            arrest = input("직업을 알고싶은사람 선택하세요 ex)1")
            while(i<8):
                if arrest == i:
                    print("지목한 ", arrest , " 직업은 " , userjobsetlist[i] , " 입니다.")
                    arrestResult = i
                break
            i=i+1

            




    elif temp == 6:
        print("아침입니다. 임무목표를 수행하세요.")
    elif temp == 16:
        print("투표시간입니다.")
    elif temp == 17:
        print(" 최후의 반론")
    elif temp == 10:
        print(" 최종 투표")
    
    while (sec !=0):
        sec = sec-1
        time.sleep(1)
        print(sec)
    


def DateResult(killResult,arrestResult):
    print("죽은사람 : " , killResult, " , 경찰이 검거한사람 : " , arrestResult)
    


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




while(1): # 타이머 주기
    print("내직업 현재 :",myjob)
    timer(5,myjob) # 밤 실행
    DateResult(killResult,arrestResult)

    
    if mafia_su==0 or mafia_su==citizen_su: #밤 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break
   
    timer(6,myjob) # 아침 실행

    
    if mafia_su==0 or mafia_su==citizen_su :#아침 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(16,myjob) # 투표 실행

    if mafia_su==0 or mafia_su==citizen_su: #투표 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(17,myjob) # 반론 실행

    if mafia_su==0 or mafia_su==citizen_su: #반론 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(10,myjob) # 최종투표 실행

    if mafia_su==0 or mafia_su==citizen_su: #최종투표 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break



if(mafia_su==0):
    print("시민팀 승리")

elif mafia_su==citizen_su:
    print("마피아팀 승리")





###############################

