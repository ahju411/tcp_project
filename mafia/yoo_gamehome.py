# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Temp\gamehome.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChattingText = QtWidgets.QTextEdit(self.centralwidget)
        self.ChattingText.setGeometry(QtCore.QRect(10, 10, 441, 441))
        self.ChattingText.setObjectName("ChattingText")
        self.InputChatting = QtWidgets.QLineEdit(self.centralwidget)
        self.InputChatting.setGeometry(QtCore.QRect(10, 460, 371, 20))
        self.InputChatting.setObjectName("InputChatting")
        self.Chatting_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Chatting_Button.setGeometry(QtCore.QRect(390, 460, 61, 23))
        self.Chatting_Button.setObjectName("Chatting_Button")
        self.user_myname = QtWidgets.QLabel(self.centralwidget)
        self.user_myname.setGeometry(QtCore.QRect(460, 60, 101, 16))
        self.user_myname.setObjectName("user_myname")
        self.skill_to_user1 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user1.setGeometry(QtCore.QRect(490, 330, 41, 21))
        self.skill_to_user1.setObjectName("skill_to_user1")
        self.skill_to_user8 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user8.setGeometry(QtCore.QRect(540, 420, 41, 21))
        self.skill_to_user8.setObjectName("skill_to_user8")
        self.skill_to_user4 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user4.setGeometry(QtCore.QRect(540, 360, 41, 21))
        self.skill_to_user4.setObjectName("skill_to_user4")
        self.skill_to_user2 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user2.setGeometry(QtCore.QRect(540, 330, 41, 21))
        self.skill_to_user2.setObjectName("skill_to_user2")
        self.skill_to_user3 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user3.setGeometry(QtCore.QRect(490, 360, 41, 21))
        self.skill_to_user3.setObjectName("skill_to_user3")
        self.skill_to_user5 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user5.setGeometry(QtCore.QRect(490, 390, 41, 21))
        self.skill_to_user5.setObjectName("skill_to_user5")
        self.skill_to_user6 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user6.setGeometry(QtCore.QRect(540, 390, 41, 21))
        self.skill_to_user6.setObjectName("skill_to_user6")
        self.skill_to_user7 = QtWidgets.QPushButton(self.centralwidget)
        self.skill_to_user7.setGeometry(QtCore.QRect(490, 420, 41, 21))
        self.skill_to_user7.setObjectName("skill_to_user7")
        self.skill_user_info = QtWidgets.QLabel(self.centralwidget)
        self.skill_user_info.setGeometry(QtCore.QRect(490, 310, 101, 16))
        self.skill_user_info.setObjectName("skill_user_info")
        self.user_job = QtWidgets.QLabel(self.centralwidget)
        self.user_job.setGeometry(QtCore.QRect(460, 150, 121, 20))
        self.user_job.setObjectName("user_job")
        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(460, 20, 91, 16))
        self.Date.setObjectName("Date")
        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(570, 20, 56, 12))
        self.Timer.setObjectName("Timer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Chatting_Button.setText(_translate("MainWindow", "전송"))
        self.user_myname.setText(_translate("MainWindow", "유저1(자기이름)"))
        self.skill_to_user1.setText(_translate("MainWindow", "유저1"))
        self.skill_to_user8.setText(_translate("MainWindow", "유저8"))
        self.skill_to_user4.setText(_translate("MainWindow", "유저4"))
        self.skill_to_user2.setText(_translate("MainWindow", "유저2"))
        self.skill_to_user3.setText(_translate("MainWindow", "유저3"))
        self.skill_to_user5.setText(_translate("MainWindow", "유저5"))
        self.skill_to_user6.setText(_translate("MainWindow", "유저6"))
        self.skill_to_user7.setText(_translate("MainWindow", "유저7"))
        self.skill_user_info.setText(_translate("MainWindow", "투표or능력사용l"))
        self.user_job.setText(_translate("MainWindow", "자기 직업사진 뜨는곳"))
        self.Date.setText(_translate("MainWindow", "1번째 밤입니다."))
        self.Timer.setText(_translate("MainWindow", "00:15"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
