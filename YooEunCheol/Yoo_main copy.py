
import time
import threading
import random
from threading import *



def startTimer():
    global i
    print(i)
    i-=1
    timer = threading.Timer(1, startTimer)
    timer.start()
    if i==0 :
        timer.cancel()
        return i
 
i=3
startTimer()

    
