import random

## 게임 들어오면 직업을 부여, 8명될경우 게임 시작

player = ["","","","","","","",""]
count = 0
for i in player:
    num = random.sample(range(0,1))
    player[0] = num
for j in player:
    if player[j] == 1 :
        count = count + 1
        if count == 2 :
            player[j] = ""
            i = i - 1


print(player[0] , player[1] , player[2]
, player[3], player[4], player[5], player[6], player[7], player[8])
            
    


def Ifwin(Mafia_su,Citizen_su): # 마피아, 시민팀 승리조건
    
    if Mafia_su==Citizen_su :
        print("Mafia Team Win ")

    elif Mafia_su==0 :
        print("Citizen Team Win")