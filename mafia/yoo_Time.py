# 



import random
import threading


count=0


# 타이머
def start_timer(count):

    count-=1
    print(count)
    timer=threading.Timer(1,start_timer,args=[count])
    timer.start()

    if count ==0 :
        print('시간이 지났습니다.')
        timer.cancel()



# 타이머 주기 계획
# start_timer(30)   30초 타이머 <밤>
# start_timer(120) 120초 타이머 < 아침 >
# start_timer(15) 15초 타이머 < 투표시간 >
# start_timer(30) 30초 타이머 < 최후의 반론 >
# start_timer(15) 15초 타이머 < 최후의 투표 >


#################################################################

# 0 게임 대기중 1.2 마피아 3 경찰 4 의사 5 시민

# 게임 대기중일때
class USER_GAMEINFO:
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



## 직업 랜덤부여 

user = ["","","","","","","",""]
joblist = [1,2,3,4,5,6,7,8]
joblist = random.sample(joblist,8)
i=0
while(i<8):
    nickname = (input('닉네임 입력: '))
    user[i] = USER_GAMEINFO(nickname,joblist)
    i=i+1



user1 = USER_GAMEINFO(user[0],joblist[0])
user2 = USER_GAMEINFO(user[1],joblist[1])
user3 = USER_GAMEINFO(user[2],joblist[2])
user4 = USER_GAMEINFO(user[3],joblist[3])
user5 = USER_GAMEINFO(user[4],joblist[4])
user6 = USER_GAMEINFO(user[5],joblist[5])
user7 = USER_GAMEINFO(user[6],joblist[6])
user8 = USER_GAMEINFO(user[7],joblist[7])

# 게임 시작시


print(user1.nickname ," , " , user1.job)
print(user2.nickname ," , " , user2.job)
print(user3.nickname ," , " , user3.job)
print(user4.nickname ," , " , user4.job)
print(user5.nickname ," , " , user5.job)
print(user6.nickname ," , " , user6.job)
print(user7.nickname ," , " , user7.job)
print(user8.nickname ," , " , user8.job)
