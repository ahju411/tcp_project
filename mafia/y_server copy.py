import socket
import threading
import random
import time
UserList = []
joblist = ["마피아","경찰"]  
Start_Num = 0
UserJobList=[]

class Server(object):
    def __init__(self, hostname, port):
        self.clients = {}
        
        
        

        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # start server####aaaa
        self.tcp_server.bind((hostname, port))
        self.tcp_server.listen(5)

        print("[INFO] Server running on {}:{}".format(hostname, port))


        
        while True: ##  게임 대기문 
            connection, address = self.tcp_server.accept()
            nickname = connection.recv(1024)
            nickname = nickname.decode()
            self.clients[nickname] = connection
            
            # start a thread for the client
            threading.Thread(target=self.receive_message, args=(connection, nickname), daemon=True).start()

            UserList.append(nickname)
            

            self.send_Enter_message("님이 입장하셨습니다 .",nickname)
            
            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))

            if len(UserList) ==2:
                break
        #게임 세팅
        
        

       
        threading.Thread(target=self.receive_message, args=(connection, nickname), daemon=True).start()
        self.send_Enter_message("\n"+"게임 시작합니다","<시스템>")
        time.sleep(1)

        
       # 버튼에 유저이름 새기기 이거왜 안되냐 일단 보류
      #  self.send_Username_Button_Setting(UserList[0])
       # self.send_Username_Button_Setting(UserList[1]) 

        global joblist ## 직업분배하는곳
        joblist=random.sample(joblist,2)
        self.send_Job_message(UserList[0])
        self.send_Job_message(UserList[1])
        self.send_Enter_message("\n직업 분배중입니다.","<시스템>")
        time.sleep(5)
       
        while True:  # 게임시작

            # 1. 밤 # 30초

            ## 타이머 스레드 생성
            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n밤입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("밤") ## 각 클라이언트에게 밤을 표시하도록 함.
            ## 타이머 스레드 시작
            T1.start()
            T2.start()
            
            

            time.sleep(9) ## + 2초 대기

            ## 밤 사이에 있던 상호작용 처리하기


          

            time.sleep(1)
            # 2. 아침 ( 대화 시간 ) # 120초


            ## 타이머 스레드 생성
            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n아침입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("아침") ## 각 클라이언트에게 밤을 표시하도록 함.
            ## 타이머 스레드 시작
            T1.start()
            T2.start()


            time.sleep(9)


            time.sleep(1)


            # 3. 투표시간 15초

            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n투표시간입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("투표시간") ## 각 클라이언트에게 밤을 표시하도록 함.
            ## 타이머 스레드 시작
            T1.start()
            T2.start()
            
            time.sleep(9)

            time.sleep(1)



            # 4. 최후의 반론 15초

            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n최후의반론입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("최후의반론") ## 각 클라이언트에게 밤을 표시하도록 함.
            ## 타이머 스레드 시작
            T1.start()
            T2.start()

            time.sleep(9)

            time.sleep(1)

             # 5. 최후의 투표 15초

            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n최종 투표시간입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("최종투표") ## 각 클라이언트에게 밤을 표시하도록 함.
            ## 타이머 스레드 시작
            T1.start()
            T2.start()

            time.sleep(9)

            time.sleep(1)


      

    def receive_message(self, connection, nickname): ## 서버에서 보낸 메시지 받기
        print("[INFO] Waiting for messages")
        while True:
            try:
                msg = connection.recv(1024)
                
                self.send_message(msg, nickname)
                print(nickname + ": " + msg.decode())
            except:
                connection.close()

                #remove user from users list
                del(self.clients[nickname])

                break

        print(nickname, " disconnected")

    def send_Username_Button_Setting(self,nickname):
        for i in range(0,len(UserList)):
            if UserList[i]==nickname:
                for i in range(0,len(UserList)):
                    msg=str(UserList[i])+"%!"
                    self.clients[nickname].send(msg.encode())

    
    def send_Timer_message(self,nickname,sec): ## 타이머 보내기
         for i in range(0,len(UserList)):
            if UserList[i] == nickname:
                while sec!=0:
                    sec-=1
                    sec=str(sec)
                    msg = "00:"+sec+"초#!"
                    self.clients[nickname].send(msg.encode())
                    sec=int(sec)
                    time.sleep(1)

    def send_Date_message(self,Date): ## 밤,아침,투표시간 등등 보내기
         if len(self.clients) >0:
            for nickname in self.clients:
                msg = str(Date)+"입니다."+"#@"
                self.clients[nickname].send(msg.encode())

    def send_Enter_message(self,message,entname): ## 누가 입장했는지 표시
        if len(self.clients) >0:
            for nickname in self.clients:
                msg = entname + ": " + message
                self.clients[nickname].send(msg.encode())

    def send_Job_message(self,nickname): ## 직업알려주기
        if len(self.clients) >0:
            for i in range(0,len(UserList)):
                if UserList[i] == nickname:
                    msg = "\n당신의 직업은 : " + str(joblist[i]) + "입니다."
                    if str(joblist[i]) == "마피아":
                        msg+="!@"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "!" and msg[-1] =="@":
                            msg = "죽일 사람을 지목하세요. 기회는 단 한번입니다."
                            self.clients[nickname].send(msg.encode())
                    elif str(joblist[i]) == "경찰":
                        msg+="@!"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "@" and msg[-1] =="!":
                            msg = "정체를 알고싶은사람을 지목하세요."
                            self.clients[nickname].send(msg.encode())


    def send_message(self, message, sender): ## 유저들간 채팅보내기
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())


    


if __name__ == "__main__":
    port = 9090
    hostname = "localhost"

    chat_server = Server(hostname, port)