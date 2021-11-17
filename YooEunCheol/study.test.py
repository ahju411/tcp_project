import threading
import os
 
 
class MainClass():
 
    def __init__(self):
        #self.threadctl = threading.Thread(target=self.subthread(1))
        self.num=0
        
        # Thread 대신에 Timer사용
        # interval(sec) 만큼 이후에 함수 실행함
        self.threadctl = threading.Timer(interval=2, function=self.subthread, args=(1,))
 
        self.threadctl.start()
 
    def subthread(self,task):
        if(self.num <5) :
            self.num=self.num+1
            print("thread end")
            
            # 함수 안에서 다시 정의 및 start()
            self.threadctl = threading.Timer(interval=2, function=self.subthread, args=(1,))
            self.threadctl.start()
 
if (__name__ == "__main__"):
    mainclass = MainClass()