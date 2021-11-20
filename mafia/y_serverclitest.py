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
            
            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")
            
            

            

        
            




        



    def show_message(self, message):
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