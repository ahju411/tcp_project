import socket
import threading
import random
import time
from types import DynamicClassAttribute
from typing import Final

UserList = []
joblist = ["마피아","경찰","의사"]  
Start_Num = 0
UserJobList=[]
user_toVote=["","",""]
Votelist=[0,0,0]
FinalVotelist=["","",""]

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
            #Votelist.append(0)
            global Date
            Date="대기중"
            

            self.send_Enter_message("님이 입장하셨습니다 .",nickname)
            
            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))

            if len(UserList) ==3: ## n명되면 게임대기문 빠져나옴
                break

        #게임 세팅
       
        
        self.send_Enter_message("\n"+"게임 시작합니다","<시스템>")
        time.sleep(1)
        global police_skill,doctor_skill,mafia_kill,mafia_su,citizen_su
        global Vote_Y
        global Vote_N
        global VoteMax,vote_equ_flag,max_equ_num
        global FinalVoteUser
        vote_equ_flag=0
        VoteMax=-1
        mafia_kill=""
        police_skill=""
        doctor_skill=""
        FinalVoteUser=""
        mafia_su=1
        citizen_su=5
        Vote_Y=0
        Vote_N=0
        max_equ_num=-1

       
       
       # 버튼에 유저이름 새기기 이거왜 안되냐 일단 보류
      #  self.send_Username_Button_Setting(UserList[0])
       # self.send_Username_Button_Setting(UserList[1]) 

        global joblist ## 직업분배하는곳
        self.send_Enter_message("직업 분배중입니다.\n","<시스템>")
        joblist=random.sample(joblist,3)
        self.send_Job_message(UserList[0]) ## ↓각 유저들에게 직업을 알려줍니다
        self.send_Job_message(UserList[1])
        self.send_Job_message(UserList[2])
        
        time.sleep(5)

        
       
        while True:  # 게임시작

            # 1. 밤 # 30초

            ## 타이머 스레드 생성
            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            T3=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("밤입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("밤") ## 각 클라이언트에게 밤을 표시하도록 함.
            
            Date="밤"
            ## 타이머 스레드 시작
            T1.start()
            T2.start()
            T3.start()
            
            
            
            time.sleep(9) ## + 2초 대기
            print("마피아킬 여전하냐?",mafia_kill)
            print("경찰지목 여전하냐?",police_skill)
            print("의사지목 여전하냐?",doctor_skill)
            ## 밤 사이에 있던 상호작용 처리하기

            
            
            if mafia_kill == doctor_skill: ## 마피아지목==의사지목 = 살인실패
                self.send_Enter_message("누군가가 마피아로의 공격으로부터 살아남았습니다.!","<시스템>")
                
            elif mafia_kill != doctor_skill: ## 마피아지목!=의사지목
                self.send_Enter_message(mafia_kill,"<시스템> 밤에 습격을 당한사람")
                for i in range(0,len(UserList)): # 
                     if UserList[i] ==  mafia_kill:
                         nickname=mafia_kill
                         joblist[i] = "사망"
                         citizen_su-=1
                         msg="당신은 밤에 습격을 당했습니다."
                         self.clients[nickname].send(msg.encode()) ## 살해당한 유저에게 죽었다고 보냅니다

            else:
                self.send_Enter_message("아무런 일이 일어나지 않았습니다.","<시스템>")

            time.sleep(1)
            # 2. 아침 ( 대화 시간 ) # 120초
           

            ## 타이머 스레드 생성
            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            T3=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("아침입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("아침") ## 각 클라이언트에게 밤을 표시하도록 함.
            Date="아침"
            ## 타이머 스레드 시작
            T1.start()
            T2.start()
            T3.start()


            time.sleep(9)


            time.sleep(1)


            # 3. 투표시간 15초

            T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            T3=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            self.send_Enter_message("\n투표시간입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            self.send_Date_message("투표시간") ## 각 클라이언트에게 밤을 표시하도록 함.
            Date="투표시간"
            ## 타이머 스레드 시작
            T1.start()
            T2.start()
            T3.start()
            
            time.sleep(9)
            ## 투표간 상호작용 처리
            for i in range(0,len(UserList)):
                for name in user_toVote:
                   if UserList[i] == name:
                       Votelist[i] +=1


                
            
            print("votelist ==",Votelist)
                


            for i in range(0,len(UserList)):
                if VoteMax < Votelist[i]:
                    VoteMax = Votelist[i]
                    if max_equ_num < VoteMax:
                        vote_equ_flag==0
                elif VoteMax == Votelist[i]:
                    vote_equ_flag==1
                    max_equ_num=VoteMax
            
            print("투표현황좀보자 :",user_toVote)
            print("투표 수 ",Votelist)
            for i in range(0,len(UserList)):
                if Votelist[i]==VoteMax and vote_equ_flag==1:
                    self.send_Enter_message("투표 결과 동률입니다.","<시스템>")
                elif Votelist[i]==VoteMax and vote_equ_flag==0:
                    FinalVoteUser=UserList[i]
                    print("최종투표후보자 : ",FinalVoteUser)
                    self.send_Enter_message(UserList[i],"<시스템> 투표로 지목 받은사람 : ")

            
            time.sleep(2)



            # 4. 최후의 반론 15초
            if vote_equ_flag==0:
                T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
                T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                T3=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                self.send_Enter_message("\n최후의반론입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
                self.send_Date_message("최후의반론") ## 각 클라이언트에게 밤을 표시하도록 함.
                Date="최후의반론"
                ## 타이머 스레드 시작
                T1.start()
                T2.start()
                T3.start()

                time.sleep(9)
                



                time.sleep(1)

                # 5. 최후의 투표 15초

               # self.send_FinalVote_Popup(UserList[0]) #팝업 어캐하노
               # self.send_FinalVote_Popup(UserList[1])
               # self.send_FinalVote_Popup(UserList[2])

                T1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
                T2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                T3=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                self.send_Enter_message("최종 투표시간입니다. 입력방법 : /Y or /N","<시스템>") # 전체채팅에 밤입니다 라고 알림.
                self.send_Date_message("최종투표") ## 각 클라이언트에게 밤을 표시하도록 함.
                Date="최후의투표"
                ## 타이머 스레드 시작
                T1.start()
                T2.start()
                T3.start()

                time.sleep(9)
                # 최후의 투표 결과 처리
                for i in range(0,len(FinalVotelist)):
                    if FinalVotelist[i] =="Y":
                        Vote_Y+=1
                    elif FinalVotelist[i] == "N":
                        Vote_N+=1
               

                if Vote_Y > Vote_N:
                    self.send_Enter_message("님은 최종 투표 결과로 인해 죽었습니다.",FinalVoteUser)
                    for i in range(0,len(UserList)): # 
                     if UserList[i]== FinalVoteUser:
                        joblist[i] = "사망"
                        citizen_su-=1
                        msg="당신은 투표로 인해 죽었습니다."
                        print("작동하나유유유유유",nickname,joblist[i],FinalVoteUser)
                        self.clients[FinalVoteUser].send(msg.encode()) ## 유저에게 죽었다고 보냅니다
                
                elif Vote_Y <= Vote_N:
                    self.send_Enter_message("최종 투표결과 아무런일이 일어나지 않았습니다.","<시스템>")

                time.sleep(1)

            else:
                self.send_Enter_message("투표 결과 아무런 일이 일어나지않았습니다.","<시스템>")


      
    def receive_message(self, connection, nickname): ## 클라로부터 메시지 받기
        print("[INFO] Waiting for messages")
        while True:
            try:
                global mafia_kill,police_skill,doctor_skill,Votelist,FinalVotelist
                msg = connection.recv(1024)

                dmsg = msg.decode()
                print("닉네임 :",nickname,"받은것",dmsg)
                print(dmsg[-2])
               

                # 클라에서 받은게 Button이벤트 일경우~~~
                if Date=="밤" and dmsg[-2]=="%":  # %는 버튼코드 , 밤일경우 각 버튼은 직업스킬로 바뀜

                    for i in range(0,len(UserList)):
                        if UserList[i] == nickname and joblist[i]=="마피아": ## 밤인데 마피아가 지목을했다면?
                            mafia_kill=dmsg[0:-2]

                    for i in range(0,len(UserList)):
                        if UserList[i] == nickname and joblist[i]=="경찰": ## 밤인데 경찰이 지목을했다면?
                            police_skill=dmsg[0:-2]

                            for i in range(0,len(UserList)): # 경찰은 지목한사람 직업을 바로보낸다.
                                if UserList[i] ==  police_skill:
                                    dmsg =police_skill+"의 직업은"+str(joblist[i])+" 입니다.\n"
                                    self.clients[nickname].send(dmsg.encode())
                                   

                    for i in range(0,len(UserList)):
                        if UserList[i] == nickname and joblist[i]=="의사": ## 밤인데 의사가 지목을했다면?
                            doctor_skill=dmsg[0:-2]
                
                elif Date=="투표시간" and dmsg[-2]=="%":
                     print("여기가문제냐?????? Date : ",Date," dmsg = ",dmsg[0:-2])
                     for i in range(0,len(UserList)):
                        if UserList[i] == nickname:
                            user_toVote[i]=dmsg[0:-2]
                            dmsg=str(UserList[i])+"님을 투표 했습니다."

                elif Date=="최후의투표" and dmsg[-2]=="/":
                    if dmsg[-1]=="Y":
                        for i in range(0,len(UserList)):
                            if UserList[i] == nickname:
                                FinalVotelist[i]="Y"
                                dmsg="찬성 했습니다."
                                self.clients[nickname].send(dmsg.encode())

                    elif dmsg[-1]=="N":
                        for i in range(0,len(UserList)):
                            if UserList[i] == nickname:
                                FinalVotelist[i]="N"
                                dmsg="반대 했습니다."
                                self.clients[nickname].send(dmsg.encode())

                
                self.send_message(msg, nickname)
                print(nickname + ": " + msg.decode())
            except:
                connection.close()

                #remove user from users list
                del(self.clients[nickname])

                break

        print(nickname, " disconnected")

    #def send_FinalVote_Popup(self,nickname): ## 팝업어캐하노
        # if len(self.clients) >0:
          #  for nickname in self.clients:
           #     msg ="*!"
               # self.clients[nickname].send(msg.encode())


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
                    elif str(joblist[i]) == "의사":
                        msg+="@@"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "@" and msg[-1] =="@":
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