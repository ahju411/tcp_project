
import time

mafia_su=2
citizen_su=4

def timer(sec):
    temp=sec
    global gamemode

  

    if temp == 5 :
        print("밤입니다. 스킬을 사용하세요.")
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
    
    
#######

while(1): # 타이머 주기

    timer(5) # 밤 실행

    
    if mafia_su==0 or mafia_su==citizen_su: #밤 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break
   
    timer(6) # 아침 실행

    
    if mafia_su==0 or mafia_su==citizen_su :#아침 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(16) # 투표 실행

    if mafia_su==0 or mafia_su==citizen_su: #투표 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(17) # 반론 실행

    if mafia_su==0 or mafia_su==citizen_su: #반론 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

    timer(10) # 최종투표 실행

    if mafia_su==0 or mafia_su==citizen_su: #최종투표 끝나고 마피아수, 시민수 체크해서 동일하면 타이머 주기 끝
        gamemode = 0
        break

###########

if(mafia_su==0):
    print("시민팀 승리")

elif mafia_su==citizen_su:
    print("마피아팀 승리")





