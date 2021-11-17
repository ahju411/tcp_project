
import time

mafia_su=2
citizen_su=4

import threading
 

Date = "night"
DateCh=0
a="b"
def startTimer():
    global i
    global Date
    print(i)
    i-=1
    timer = threading.Timer(1, startTimer)
    timer.start()

    if i==0:
        Date="apapap"

        timer.cancel()
        
      
        


if Date=="night":
    i=3
    print("밤입니다.")
    startTimer() # 게임시간 Start
    time.sleep(5)


        
    

    






