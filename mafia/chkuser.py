#가입정보 확인창
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res,dao


class Ui_chkuser(QtWidgets.QWidget):
    command = QtCore.pyqtSignal(str)
    def __init__(self):
            super(Ui_chkuser,self).__init__()
            self.openWindow()
            self.show()
    def openWindow(self):
            self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 191)
        Form.move(1150,350)
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
        self.label.setStyleSheet("background-color:rgba(230,230,230,180);\n"
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
"border-bottom:2px solid rgba(0,0,3,180);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,3,180);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 100, 51, 20))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,3,180);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 100, 51, 20))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,3,180);\n"
"color:rgba(0,0,0,230);\n"
"padding-bottom:5px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(93, 70, 16, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(153, 70, 16, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 75, 51))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(0,0,0);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.chkuser)
        self.lineEdit_4.returnPressed.connect(self.chkuser)


    def chkuser(self):
            from changepw import Ui_changepw
            
            chkid = self.lineEdit.text()
            self.command.emit(chkid)
            tel = self.lineEdit_2.text() + self.lineEdit_3.text() + self.lineEdit_4.text()
            value = (chkid,tel)
            if dao.chkuser(value) == 0: #확인~ 
                    self.cpw = Ui_changepw()
                    self.cpw.show()
                    self.cpw.receivevalue(chkid)
                    self.close()

            else:
                    QtWidgets.QMessageBox.about(self,"알림","존재하지 않는 정보입니다.")







    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "ID"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Tel"))
        self.label_2.setText(_translate("Form", "-"))
        self.label_3.setText(_translate("Form", "-"))
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_3.setMaxLength(4)
        self.lineEdit_4.setMaxLength(4)
        self.label_4.setText(_translate("Form","가입정보확인"))

if __name__=='__main__':
        QtWidgets.QApplication.processEvents()
        app = QtWidgets.QApplication(sys.argv)
        chkuser = Ui_chkuser()
        chkuser.show()
        sys.exit(app.exec_())
