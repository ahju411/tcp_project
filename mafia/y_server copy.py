import socket
import threading
import random
import time
from types import DynamicClassAttribute
from typing import Final
'''
/Y
/N    투표YES NO 

#! 타이머
#@ Date

직업알리기
!@ 마피아1
!# 마피아2
@! 경찰
@@ 의사
@# 시민1
@$ 시민2
@% 시민3
@^ 시민4

% 버튼클릭 
%! USER1
%@ USER2
%# USER3
%$ USER4
%^ USER5
%& USER6
%* USER7
%( USER8

^! 마피아1 KILL 작용
^@ 마피아2KILL작용 << 이건 안쓰임 마피아 하나라
^# 경찰작용
^^ 의사 작용

*! 지목버튼에 이름새길때 전달코드
*@ 채팅버튼 세팅할때 전달코드




'''
UserList = []
joblist = ["마피아","마피아","경찰","의사","시민","시민"]  
Start_Num = 0
UserJobList=[]
user_toVote=["","","","","",""]
Votelist=[0,0,0,0,0,0]
FinalVotelist=["","","","","",""]

class Server(object):
    def __init__(self, hostname, port):
        self.clients = {}
        global currentusernum # 사람이 몇명있는지 확인하는 변수
        currentusernum =0
        
        
        

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
            Date="게임세팅"
            self.send_ChatButton_Setting(Date)
            

            self.send_Enter_message("님이 입장하셨습니다 .",nickname)
            
            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))

            if nickname in UserList: # 현재 닉네임이 있으면 현재유저에 추가
                currentusernum+=1
                print(currentusernum)

            if currentusernum ==6: ##n명되면 게임대기문 빠져나옴
                break

        #게임 세팅
       
        
        self.send_Enter_message("\n게임 시작합니다","<시스템>")
        
        
        global police_skill,doctor_skill,mafia_kill,mafia_su,citizen_su
        global Vote_Y
        global Vote_N
        global VoteMax,vote_equ_flag,max_equ_num
        global FinalVoteUser
        vote_equ_flag=0
        VoteMax=-1
        
        FinalVoteUser=""
        mafia_su=2
        citizen_su=4
        Vote_Y=0
        Vote_N=0
        max_equ_num=-1
        time.sleep(3)
        
        self.send_Enter_message("\n게임 세팅중입니다..","<시스템>")
        self.send_Username_Button_Setting(UserList[0])
        self.send_Username_Button_Setting(UserList[1])
        self.send_Username_Button_Setting(UserList[2])
        self.send_Username_Button_Setting(UserList[3])
        self.send_Username_Button_Setting(UserList[4])
        self.send_Username_Button_Setting(UserList[5])

        time.sleep(2)
       
        
       
       # 버튼에 유저이름 새기기 이거왜 안되냐 일단 보류
      #  self.send_Username_Button_Setting(UserList[0])
       # self.send_Username_Button_Setting(UserList[1]) 

        global joblist ## 직업분배하는곳
        global Mafia
        self.send_Enter_message("직업 분배중입니다.","<시스템>")
        time.sleep(3)
        joblist=random.sample(joblist,6)
        self.send_Job_message(UserList[0]) ## ↓각 유저들에게 직업을 알려줍니다
        self.send_Job_message(UserList[1])
        self.send_Job_message(UserList[2])
        self.send_Job_message(UserList[3])
        self.send_Job_message(UserList[4])
        self.send_Job_message(UserList[5])
        

        for i in range(0,len(joblist)): ## 게임 종료후에 마피아가 누군지 알려주기위해 마피아값을 구한다.
            if joblist[i]=="마피아":
                Mafia=UserList[i]
      
        
        time.sleep(3)

        
       
        while True:  # 게임시작

            # 1. 밤 # 30초
            mafia_kill=""
            police_skill=""
            doctor_skill=""
            
            self.send_Enter_message("밤입니다. 활동을 진행해주세요.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            time.sleep(1)
            Date="밤"
            self.send_ChatButton_Setting(Date) #밤에는 채팅못치도록 버튼 세팅코드 보냄
            self.send_Date_message("밤") ## 각 클라이언트에게 밤을 표시하도록 함.
           # self.send_Enter_message("아무런 일이 일어나지 않았습니다.","<시스템>")
            ## 타이머 스레드 생성
            Tnight1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            Tnight2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            Tnight3=threading.Thread(target=self.send_Timer_message, args=(UserList[2], 7), daemon=True)
            Tnight4=threading.Thread(target=self.send_Timer_message, args=(UserList[3], 7), daemon=True)
            Tnight5=threading.Thread(target=self.send_Timer_message, args=(UserList[4], 7), daemon=True)
            Tnight6=threading.Thread(target=self.send_Timer_message, args=(UserList[5], 7), daemon=True)
            
            ## 타이머 스레드 시작
            Tnight1.start()
            Tnight2.start()
            Tnight3.start()
            Tnight4.start()
            Tnight5.start()
            Tnight6.start()
            
            
            time.sleep(8) ## + 2초 대기
            ## 밤 사이에 있던 상호작용 처리하기

            
            
            if mafia_kill == doctor_skill: ## 마피아지목==의사지목 = 살인실패
                if mafia_kill =="" and doctor_skill=="":
                    self.send_Enter_message("아무런 일이 일어나지 않았습니다.","<시스템>")
                else:
                    self.send_Enter_message("누군가가 마피아로의 공격으로부터 살아남았습니다.!","<시스템>")
                
            elif mafia_kill != doctor_skill: ## 마피아지목!=의사지목
                self.send_Enter_message(mafia_kill,"<시스템> 밤에 습격을 당한사람")
                for i in range(0,len(UserList)): # 
                    if UserList[i] ==  mafia_kill:
                        if Mafia==mafia_kill:
                            joblist[i]="사망"
                            mafia_su-=1
                            msg="<시스템>:당신은 밤에 습격을 당했습니다."
                            self.clients[Mafia].send(msg.encode()) ## 살해당한 유저에게 죽었다고 보냅니다
                        else:
                            nickname=mafia_kill
                            joblist[i] = "사망"
                            citizen_su-=1
                            msg="<시스템>:당신은 밤에 습격을 당했습니다."
                            self.clients[mafia_kill].send(msg.encode()) ## 살해당한 유저에게 죽었다고 보냅니다

            else:
                self.send_Enter_message("아무런 일이 일어나지 않았습니다.","<시스템>")

            time.sleep(3)

            if mafia_su==0 or citizen_su==mafia_su: ## 게임종료조건이 되면 게임을끝냅니다
                break

           



            # 2. 아침 ( 대화 시간 ) # 120초
           

            ## 타이머 스레드 생성
            
            self.send_Enter_message("아침입니다. 대화를 나눠주세요.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            time.sleep(1)
            Date="아침"
            self.send_ChatButton_Setting(Date) # 아침 채팅 세팅
            self.send_Date_message("아침") ## 각 클라이언트에게 밤을 표시하도록 함.
            

            Tmorning1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            Tmorning2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            Tmorning3=threading.Thread(target=self.send_Timer_message, args=(UserList[2], 7), daemon=True)
            Tmorning4=threading.Thread(target=self.send_Timer_message, args=(UserList[3], 7), daemon=True)
            Tmorning5=threading.Thread(target=self.send_Timer_message, args=(UserList[4], 7), daemon=True)
            Tmorning6=threading.Thread(target=self.send_Timer_message, args=(UserList[5], 7), daemon=True)
            ## 타이머 스레드 시작
            Tmorning1.start()
            Tmorning2.start()
            Tmorning3.start()
            Tmorning4.start()
            Tmorning5.start()
            Tmorning6.start()


            time.sleep(8)
            

            # 3. 투표시간 15초
            Votelist=[0,0,0,0,0,0]
            self.send_Enter_message("투표시간입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
            time.sleep(1)
            Date="투표시간"
            self.send_ChatButton_Setting(Date) # 투표시간 채팅 세팅
            self.send_Date_message("투표시간") ## 각 클라이언트에게 밤을 표시하도록 함.
            Tvote1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
            Tvote2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
            Tvote3=threading.Thread(target=self.send_Timer_message, args=(UserList[2], 7), daemon=True)
            Tvote4=threading.Thread(target=self.send_Timer_message, args=(UserList[3], 7), daemon=True)
            Tvote5=threading.Thread(target=self.send_Timer_message, args=(UserList[4], 7), daemon=True)
            Tvote6=threading.Thread(target=self.send_Timer_message, args=(UserList[5], 7), daemon=True)
            
            
            
            
            ## 타이머 스레드 시작
            Tvote1.start()
            Tvote2.start()
            Tvote3.start()
            Tvote4.start()
            Tvote5.start()
            Tvote6.start()
            
            time.sleep(8)
            ## 투표간 상호작용 처리
            for i in range(0,len(UserList)):
                for name in user_toVote:
                   if UserList[i] == name:
                       Votelist[i] +=1

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
                if Votelist[i]==VoteMax and vote_equ_flag==1 and VoteMax !=0:
                    self.send_Enter_message("투표 결과 동률입니다.1","<시스템>")
                elif Votelist[i]==VoteMax and vote_equ_flag==0 and VoteMax !=0:
                    FinalVoteUser=UserList[i]
                    print("최종투표후보자 : ",FinalVoteUser)
                    self.send_Enter_message(UserList[i],"<시스템> 투표로 지목 받은사람 : ")
            
            if VoteMax==0: # 모두 투표 안했을경우
                self.send_Enter_message("투표 결과 동률입니다.2","<시스템>")

            
                

            
            time.sleep(1)



            # 4. 최후의 반론 15초
            if vote_equ_flag==0 and VoteMax!=0:
                self.send_Enter_message("최후의반론입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
                time.sleep(1)
                Date="최후의반론"
                self.send_ChatButton_Setting(Date) # 최후의반론 채팅 세팅
                self.send_Date_message("최후의반론") ## 각 클라이언트에게 밤을 표시하도록 함.
                Tlast1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
                Tlast2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                Tlast3=threading.Thread(target=self.send_Timer_message, args=(UserList[2], 7), daemon=True)
                Tlast4=threading.Thread(target=self.send_Timer_message, args=(UserList[3], 7), daemon=True)
                Tlast5=threading.Thread(target=self.send_Timer_message, args=(UserList[4], 7), daemon=True)
                Tlast6=threading.Thread(target=self.send_Timer_message, args=(UserList[5], 7), daemon=True)
                
               
                ## 타이머 스레드 시작
                Tlast1.start()
                Tlast2.start()
                Tlast3.start()
                Tlast4.start()
                Tlast5.start()
                Tlast6.start()

                time.sleep(8)

               
                



                

                # 5. 최후의 투표 15초

               # self.send_FinalVote_Popup(UserList[0]) #팝업 어캐하노
               # self.send_FinalVote_Popup(UserList[1])
               # self.send_FinalVote_Popup(UserList[2])
                self.send_Enter_message("최종 투표시간입니다. 입력방법 : /Y or /N 입니다.","<시스템>") # 전체채팅에 밤입니다 라고 알림.
                time.sleep(1)
                Date="최후의투표"
                self.send_ChatButton_Setting(Date) # 최후의투표 채팅 세팅
                self.send_Date_message("최종투표") ## 각 클라이언트에게 밤을 표시하도록 함.
                Tlastvote1=threading.Thread(target=self.send_Timer_message, args=(UserList[0], 7), daemon=True)
                Tlastvote2=threading.Thread(target=self.send_Timer_message, args=(UserList[1], 7), daemon=True)
                Tlastvote3=threading.Thread(target=self.send_Timer_message, args=(UserList[2], 7), daemon=True)
                Tlastvote4=threading.Thread(target=self.send_Timer_message, args=(UserList[3], 7), daemon=True)
                Tlastvote5=threading.Thread(target=self.send_Timer_message, args=(UserList[4], 7), daemon=True)
                Tlastvote6=threading.Thread(target=self.send_Timer_message, args=(UserList[5], 7), daemon=True)
                
                ## 타이머 스레드 시작
                Tlastvote1.start()
                Tlastvote2.start()
                Tlastvote3.start()
                Tlastvote4.start()
                Tlastvote5.start()
                Tlastvote6.start()

                time.sleep(8)
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
                            if Mafia==UserList[i]:
                                joblist[i]="사망"
                                mafia_su-=1
                                msg="<시스템>:당신은 투표로 인해 죽었습니다."
                                self.clients[Mafia].send(msg.encode()) ## 마피아 유저에게 죽었다고 보냅니다
                            else:
                                joblist[i] = "사망"
                                citizen_su-=1
                                msg="<시스템>:당신은 투표로 인해 죽었습니다."
                                print("작동하나유유유유유",nickname,joblist[i],FinalVoteUser)
                                self.clients[FinalVoteUser].send(msg.encode()) ## 유저에게 죽었다고 보냅니다
                
                elif Vote_Y <= Vote_N:
                    self.send_Enter_message("최종 투표결과 아무런일이 일어나지 않았습니다.","<시스템>")

                time.sleep(8)

                

                if mafia_su==0 or citizen_su==mafia_su: ## 게임종료조건이 되면 게임을끝냅니다
                    break

            else:
                self.send_Enter_message("투표 결과 아무런 일이 일어나지않았습니다.","<시스템>")
    
        ## 게임 종료후..

        time.sleep(1)

        Date="끝"
        self.send_ChatButton_Setting(Date) ## 자유로운 채팅
        if mafia_su==citizen_su:
            print("마피아팀의승리")
            self.send_Enter_message("\n\n\n\n","")
            self.send_Enter_message("마피아의 승리!!!!\n","<시스템>")
            self.send_Enter_message(Mafia,"<시스템>: 이번 게임의 마피아1")

        else:
            print("시민팀의승리 ")
            self.send_Enter_message("\n\n\n\n","")
            self.send_Enter_message("시민팀의 승리!!!!\n","<시스템>")
            self.send_Enter_message(Mafia,"<시스템>: 이번 게임의 마피아2")

        
        self.send_Enter_message("게임이 종료되었습니다.","\n\n\n<시스템>")


        while True: ## 자유로운 채팅~
           
            Date="끝"



      


    #################################################




    def receive_message(self, connection, nickname): ## 클라로부터 메시지 받기
        global currentusernum # 현재 유저수를 받음
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
                                    dmsg ="<시스템>:"+police_skill+"의 직업은"+str(joblist[i])+" 입니다.\n"
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
                                dmsg="<시스템>:찬성 했습니다."
                                self.clients[nickname].send(dmsg.encode())

                    elif dmsg[-1]=="N":
                        for i in range(0,len(UserList)):
                            if UserList[i] == nickname:
                                FinalVotelist[i]="N"
                                dmsg="<시스템>:반대 했습니다."
                                self.clients[nickname].send(dmsg.encode())

                
                self.send_message(msg, nickname)
                print(nickname + ": " + msg.decode())
            except:
                connection.close()
                currentusernum-=1 # 나가면 현재 유저수를 뺌

                #remove user from users list
                del(self.clients[nickname])

                break

        print(nickname, " disconnected")

    #def send_FinalVote_Popup(self,nickname): ## 팝업어캐하노
        # if len(self.clients) >0:
          #  for nickname in self.clients:
           #     msg ="*!"
               # self.clients[nickname].send(msg.encode())


    def send_Username_Button_Setting(self,nickname):  ## 버튼에 각각 유저이름 새기기
        for i in range(0,len(UserList)):
            if UserList[i]==nickname:
                for j in range(0,len(UserList)):
                    msg=str(UserList[j])+"*!"
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
                    msg = "<시스템>:당신의 직업은 : " + str(joblist[i]) + "입니다."
                    if str(joblist[i]) == "마피아":
                        msg+="!@"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "!" and msg[-1] =="@":
                            msg = "<시스템>:시민팀을 죽여 게임에 승리하세요."
                            self.clients[nickname].send(msg.encode())
                    elif str(joblist[i]) == "경찰":
                        msg+="@!"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "@" and msg[-1] =="!":
                            msg = "<시스템>:마피아의 정체를 밝혀 게임을 승리하세요"
                            self.clients[nickname].send(msg.encode())
                    elif str(joblist[i]) == "의사":
                        msg+="@@"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "@" and msg[-1] =="@":
                            msg = "<시스템>:마피아로부터 공격을 막아 게임을 승리하세요"
                            self.clients[nickname].send(msg.encode())

                    elif str(joblist[i]) == "시민":
                        msg+="@#"
                        self.clients[nickname].send(msg.encode())
                        if msg[-2] == "@" and msg[-1] =="#":
                            msg = "<시스템>:시민으로서 마피아를 찾아 승리로 이끌어주세요"
                            self.clients[nickname].send(msg.encode())        


    def send_message(self, message, sender): ## 유저들간 채팅보내기
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())

    def send_ChatButton_Setting(self,Date): ## 채팅 세팅
        print("Date 어떻게뜨죠",Date)
        if Date=="밤" or Date=="투표시간"  : ##  채팅 X 지목 O
            if len(self.clients) >0:
                for nickname in self.clients:
                    msg = "*@"
                    print("닉네임 : ",nickname,"에게",msg,"를보냈습니다.")
                    self.clients[nickname].send(msg.encode())
        elif Date=="아침" or Date=="끝" or  Date=="최후의투표" or Date =="게임세팅": ## 채팅 O 지목 X
            if len(self.clients) >0:
                for nickname in self.clients:
                    msg = "*#"
                    self.clients[nickname].send(msg.encode())
        
        elif Date=="최후의반론"  : ## 투표 지목받은사람만 채팅 O 지목 X
            if len(self.clients) >0:
                for nickname in self.clients:
                    if nickname==FinalVoteUser:
                        msg = "*#"
                        self.clients[nickname].send(msg.encode())
                    else:
                        msg="*$"  # 투표 지목 안받은사람은 채팅X 지목X
                        self.clients[nickname].send(msg.encode())
            
            

                
        


    


if __name__ == "__main__":
    port = 9090
    hostname = "0.0.0.0"
    
    chat_server = Server(hostname, port)
   