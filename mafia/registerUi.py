
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res,dao,bcrypt,chkid,chknickname
#from loginUi import Form



class Ui_registerUi(QtWidgets.QWidget):
    #def __init__(self):
         #   super().__init__
#     def openWindow(self):
#         from loginUi import Ui_Form
#         self.window = QtWidgets.QWidget()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self.window)
#         self.window.show()
    def __init__(self):
            super(Ui_registerUi,self).__init__()
            self.openWindow()
            self.show()
    def openWindow(self):
        self.setupUi(self)
        self.backbtn.clicked.connect(self.pushback) # type: ignore
    def setupUi(self, registerUi):
        registerUi.setObjectName("registerUi")
        registerUi.resize(450, 550)
        registerUi.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        registerUi.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(registerUi)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.widget.setStyleSheet("QPushButton#joinbtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.15), stop:1 rgba(255, 255, 255, 0.4));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#joinbtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.3), stop:1 rgba(255, 255, 255, 0.4));\n"
"}\n"
"QPushButton#joinbtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}\n"
"QPushButton#chkid{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.15), stop:1 rgba(255, 255, 255, 0.4));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#chkid:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.3), stop:1 rgba(255, 255, 255, 0.4));\n"
"}\n"
"QPushButton#chkid:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}\n"
"QPushButton#chknickname{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.15), stop:1 rgba(255, 255, 255, 0.4));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#chknickname:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.3), stop:1 rgba(255, 255, 255, 0.4));\n"
"}\n"
"QPushButton#chknickname:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}\n"
"QPushButton#backbtn{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#backbtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0.3), stop:1 rgba(255, 255, 255, 0.4));\n"
"}\n"
"QPushButton#backbtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/images/register.jpg);\n"
"border-radius:20px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 301, 420))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50),stop:0.835226 rgba(0,0,0,75));\n"
"border-radius: 15px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(140, 50, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(self.widget)
        self.id.setGeometry(QtCore.QRect(100, 90, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.id.setObjectName("id")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(100, 140, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.joinbtn = QtWidgets.QPushButton(self.widget)
        self.joinbtn.setGeometry(QtCore.QRect(90, 360, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.joinbtn.setFont(font)
        self.joinbtn.setStyleSheet("")
        self.joinbtn.setObjectName("joinbtn")
        self.tel1 = QtWidgets.QLineEdit(self.widget)
        self.tel1.setGeometry(QtCore.QRect(100, 230, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tel1.setFont(font)
        self.tel1.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.tel1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tel1.setObjectName("tel1")
        self.nickname = QtWidgets.QLineEdit(self.widget)
        self.nickname.setGeometry(QtCore.QRect(100, 280, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nickname.setFont(font)
        self.nickname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.nickname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nickname.setObjectName("nickname")
        self.tel2 = QtWidgets.QLineEdit(self.widget)
        self.tel2.setGeometry(QtCore.QRect(150, 230, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tel2.setFont(font)
        self.tel2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.tel2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tel2.setPlaceholderText("")
        self.tel2.setObjectName("tel2")
        self.tel3 = QtWidgets.QLineEdit(self.widget)
        self.tel3.setGeometry(QtCore.QRect(200, 230, 31, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tel3.setFont(font)
        self.tel3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.tel3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tel3.setPlaceholderText("")
        self.tel3.setObjectName("tel3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 16, 16))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(180, 250, 16, 16))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.label_6.setObjectName("label_6")
        self.chkid = QtWidgets.QPushButton(self.widget)
        self.chkid.setGeometry(QtCore.QRect(260, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setBold(False)
        font.setWeight(50)
        self.chkid.setFont(font)
        self.chkid.setObjectName("chkid")
        self.chknickname = QtWidgets.QPushButton(self.widget)
        self.chknickname.setGeometry(QtCore.QRect(250, 290, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setBold(False)
        font.setWeight(50)
        self.chknickname.setFont(font)
        self.chknickname.setObjectName("chknickname")
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setGeometry(QtCore.QRect(100, 190, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px")
        self.name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.name.setObjectName("name")
        self.backbtn = QtWidgets.QPushButton(self.widget)
        self.backbtn.setGeometry(QtCore.QRect(60, 30, 30, 30))
        self.backbtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.backbtn.setFont(font)
        self.backbtn.setObjectName("backbtn")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.id.raise_()
        self.password.raise_()
        self.joinbtn.raise_()
        self.tel1.raise_()
        self.nickname.raise_()
        self.tel2.raise_()
        self.tel3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.chkid.raise_()
        self.chknickname.raise_()
        self.name.raise_()
        self.backbtn.raise_()

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.joinbtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.retranslateUi(registerUi)
        QtCore.QMetaObject.connectSlotsByName(registerUi)
        self.joinbtn.setDisabled(True)
        #self.backbtn.clicked.connect(self.pushback) # type : ignore
        self.chkid.clicked.connect(self.chkidbtn) # type: ignore
        self.chknickname.clicked.connect(self.chknicknamebtn) # type: ignore
        self.joinbtn.clicked.connect(self.getjoinbtn) # type: ignore
    def pushback(self):
           self.close()


    def chkidbtn(self):
            #print("아이디중복확인")
            chkided = self.id.text()
            chkided1 = (chkided,)
            if chkid.login(chkided1) == True:
                    QtWidgets.QMessageBox.about(self,"알림","사용하셔도 좋습니다.")
            else:
                    QtWidgets.QMessageBox.about(self,"경고","아이디가 사용중입니다.")
                    self.id.clear()
    def chknicknamebtn(self):
            print("닉네임중복확인")
            chknicknameed = self.nickname.text()
            chknicknameed1 = (chknicknameed,)
            if chknickname.nickname(chknicknameed1)== True:
                    QtWidgets.QMessageBox.about(self,"알림","사용하셔도 좋습니다.")
            else:
                    QtWidgets.QMessageBox.about(self,"경고","닉네임이 사용중입니다.")
                    self.nickname.clear()
            self.joinbtn.setEnabled(True)
    def getjoinbtn(self):
            
            print("회원가입")
            id = self.id.text()
            pw = self.password.text()
            encode_pw = bytes(pw,'utf-8') #입력된 pw 값을 utf 8 로 인코딩하고 부호화함 
            hash_pw = bcrypt.hashpw(encode_pw,salt=bcrypt.gensalt()) #hashpw를 통해서 랜덤 해쉬값을 부여함
            name = self.name.text()
            tel1 = self.tel1.text()
            tel2 = self.tel2.text()
            tel3 = self.tel3.text()
            tel = tel1+tel2+tel3
            nickname = self.nickname.text()
            print(id,pw,tel,nickname)
            value = (id,hash_pw.decode('utf-8'),name,tel,nickname)
            if dao.insert(value) == True:
                    QtWidgets.QMessageBox.about(self,"알림","회원가입이 성공하였습니다.")
                    
            else:
                    QtWidgets.QMessageBox.about(self,"알림","회원가입이 실패하였습니다.")
    def showModal(self):
            return super().__init__


    def retranslateUi(self, registerUi):
        _translate = QtCore.QCoreApplication.translate
        registerUi.setWindowTitle(_translate("registerUi", "registerUi"))
        self.label_4.setText(_translate("registerUi", "register"))
        self.id.setPlaceholderText(_translate("registerUi", "id"))
        self.password.setPlaceholderText(_translate("registerUi", "Password"))
        self.joinbtn.setText(_translate("registerUi", "become a member"))
        self.tel1.setPlaceholderText(_translate("registerUi", "Tel"))
        self.nickname.setPlaceholderText(_translate("registerUi", "nickname"))
        self.tel1.setMaxLength(3)
        self.tel2.setMaxLength(4)
        self.tel3.setMaxLength(4)
        self.label_5.setText(_translate("registerUi", "-"))
        self.label_6.setText(_translate("registerUi", "-"))
        self.chkid.setText(_translate("registerUi", "chkid"))
        self.chknickname.setText(_translate("registerUi", "chknickname"))
        self.name.setPlaceholderText(_translate("registerUi", "name"))
        self.backbtn.setText(_translate("registerUi", "←"))
if __name__=='__main__':
        #QtWidgets.QApplication.processEvents()
        app = QtWidgets.QApplication(sys.argv)
        #registerUi = QtWidgets.QWidget()
        ui = Ui_registerUi()
      #  ui.setupUi(registerUi)
        #registerUi.show()
        app.exec()
        sys.exit(app.exec_())
