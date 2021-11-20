import socket
import threading

UserList = []
Start_Num = 0

class Server(object):
    def __init__(self, hostname, port):
        self.clients = {}
        self.id=None

        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # start server
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

            UserList.append(nickname) ## 유저닉네임을 모으는겁니다 
            
            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))
            
            if Start_Num==1:
                print("게임시작")

            if len(UserList)==8: ## 유저가 8명이면 게임 대기문 나가버리기
                break
            

            
    def send_Timer(self,Sec,sender):
        self.Sec = str(Sec)
        if len(self.clients) >0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = Sec.decode()
                    self.clients[nickname].send(msg.encode())




    def receive_message(self, connection, nickname):
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


    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())


if __name__ == "__main__":
    port = 9090
    hostname = "localhost"

    chat_server = Server(hostname, port)