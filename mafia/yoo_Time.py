
import random
import threading

count=0
Date=0
i=0
# 타이머
def start_timer(count):
    num=count
    if num == 25 :
        print("밤입니다.")
    elif num == 120:
        print("아침입니다")
    elif num == 15:
        print("투표시간입니다")
    elif num == 17:
        print(" 최후의 반론")
    elif num == 10:
        print(" 최종 투표")

    count-=1
    print(count)
    timer=threading.Timer(1,start_timer,args=[count])
    timer.start()

    if count ==0 :
        print('시간이 지났습니다.')
        timer.cancel()
    
   

# 타이머 주기 계획
# start_timer(25)   25초 타이머 <밤>
# start_timer(30) 30초 타이머 < 아침 >
# start_timer(15) 15초 타이머 < 투표시간 >
# start_timer(17) 17초 타이머 < 최후의 반론 >
# start_timer(10) 10초 타이머 < 최후의 투표 >

start_timer(25)