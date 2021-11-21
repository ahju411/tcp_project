from PyQt5 import QtCore, QtWidgets
import y_mafia_homeUI


import sys
import socket


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

        print(message)
        self.signal.emit(message)


class Client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chat_ui = y_mafia_homeUI.Ui_Mafia()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.inputbutton.clicked.connect(self.send_message)
        self.chat_ui.textEdit.returnPressed.connect(self.send_message)
        self.chat_ui.to_user1.clicked.connect(self.send_to_user1)
        self.chat_ui.to_user2.clicked.connect(self.send_to_user2)
        self.chat_ui.to_user3.clicked.connect(self.send_to_user3)
        self.chat_ui.to_user4.clicked.connect(self.send_to_user4)
        self.chat_ui.to_user5.clicked.connect(self.send_to_user5)
        self.chat_ui.to_user6.clicked.connect(self.send_to_user6)
        self.chat_ui.to_user7.clicked.connect(self.send_to_user7)
        self.chat_ui.to_user8.clicked.connect(self.send_to_user8)
        self.mainWindow.setGeometry(QtCore.QRect(500, 20,754, 595))
        

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    def btn_connect_clicked(self,myid):
        nickname = myid
        host = "localhost"
        port = 9090
        try:
            port = int(port)
        except Exception as e:
            error = "Invalid port number \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Port Number Error", error)
        
        if len(nickname) < 1:
            nickname = socket.gethostname()
 
        if self.connect(host, port, nickname):
            self.chatWidget.setVisible(True)
            self.chat_ui.myname.setText(nickname)
            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            
            print("[INFO] recv thread started")
            
            

            

        
            




        



    def show_message(self, message): ## 서버로부터 받은 메시지를 구분하는곳
        if message[-2]=="!": # 마피아팀은 [-2] == !
            if message[-1]=="@": #마피아1은 [-1] == @
                self.chat_ui.myjob_image.setText("마피아(Test)")
                message = message[0:-2]
                self.chat_ui.textBrowser.append(message)
                
            
        elif message[-2]=="@": # 시민팀은 [-2] == @
            if message[-1]=="!": # 경찰은 [-1] == !
                self.chat_ui.myjob_image.setText("경찰(Test)")
                message = message[0:-2]
                self.chat_ui.textBrowser.append(message)
                
        
        elif message[-2]=="#": # 타이머,시간은 [-2]== #
            if message[-1]=="!": # 타이머는 [-1]== ! 
                message = message[:-2] 
                self.chat_ui.Timer.setText(message)
            
            elif message[-1]=="@": # Date은 [-1] == @
                    message = message[:-2]
                    self.chat_ui.Date.setText(message)

        elif message[-2]=="%": # 이거 유저버튼클릭하면 서버로 유저버튼 넘어가는데 되돌아오는거 방지하기위해 막음
                pass

        
        else: # 일반 채팅일경우 textbroswer로 모두에게 보여줌
            self.chat_ui.textBrowser.append(message)

        

    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error)
            
            
            return False
        

    def send_to_user1(self):
        message = self.chat_ui.to_user1.text()
        message = message+"를 지목했습니다."+"%!"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]
        self.chat_ui.textBrowser.append(message)
        
    def send_to_user2(self):
        message = self.chat_ui.to_user2.text()
        message = message+"를 지목했습니다."+"%@"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)
    def send_to_user3(self):
        message = self.chat_ui.to_user3.text()
        message = message+"를 지목했습니다."+"%#"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)

    def send_to_user4(self):
        message = self.chat_ui.to_user4.text()
        message = message+"를 지목했습니다."+"%$"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)

    def send_to_user5(self):
        message = self.chat_ui.to_user5.text()
        message = message+"를 지목했습니다."+"%^"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)

    def send_to_user6(self):
        message = self.chat_ui.to_user6.text()
        message = message+"를 지목했습니다."+"%&"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]
        self.chat_ui.textBrowser.append(message)

    def send_to_user7(self):
        message = self.chat_ui.to_user7.text()
        message = message+"를 지목했습니다."+"%*"
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)

    def send_to_user8(self):
        message = self.chat_ui.to_user8.text()
        message = message+"를 지목했습니다."+"%("
        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        message = message[0:-2]    
        self.chat_ui.textBrowser.append(message)
                                        

        


    def send_message(self):
        message = self.chat_ui.textEdit.text()
        self.chat_ui.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui.textEdit.clear()

    def send_message(self):
        message = self.chat_ui.textEdit.text()
        self.chat_ui.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui.textEdit.clear()


    def show_error(self, error_type, message):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(message)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())