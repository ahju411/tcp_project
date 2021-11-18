
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res,dao,bcrypt



class Ui_changepw(QtWidgets.QWidget):

    def __init__(self):
            super(Ui_changepw,self).__init__()
            self.openWindow()
            self.show()
    def openWindow(self):
            self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 211)
        Form.move(1100,350)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 411, 181))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    image: url(:/images/images/pushbtn.png);\n"
"    border:0px\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 171))
        self.label.setStyleSheet("background-color:rgba(200,200,200,180);\n"
"border-radius:15px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,3,255);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 75, 51))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(0,0,0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 100, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,3,255);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.changepw)
        self.pushButton.clicked.connect(self.receivevalue)
        self.lineEdit_2.returnPressed.connect(self.changepw)
    def receivevalue(self,name):
            global id 
            id = name
            


    def changepw(self):
            pw = self.lineEdit.text()
            confirmpw = self.lineEdit_2.text()
            if(pw == confirmpw):
                    encode_pw = bytes(pw,'utf-8') #입력된 pw 값을 utf 8 로 인코딩하고 부호화함 
                    hash_pw = bcrypt.hashpw(encode_pw,salt=bcrypt.gensalt()) #hashpw를 통해서 랜덤 해쉬값을 부여함
                    value = (hash_pw.decode('utf-8'),id)
                    dao.changepw(value)
                    QtWidgets.QMessageBox.about(self,"알림","비밀번호가 변경되었습니다.")
                    self.close()
            else:
                    QtWidgets.QMessageBox.about(self,"알림","비밀번호가 일치하지 않습니다.")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "PW"))
        self.label_4.setText(_translate("Form", "비밀번호 변경창"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "ConfirmPW"))
if __name__=='__main__':
        QtWidgets.QApplication.processEvents()
        app = QtWidgets.QApplication(sys.argv)
        changepw = Ui_changepw()
        changepw.show()
        sys.exit(app.exec_())
