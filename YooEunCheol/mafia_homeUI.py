# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Temp\Mafia_home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import sys


class Ui_Mafia(QtWidgets.QWidget):
 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 595)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 551, 521))
        self.textBrowser.setObjectName("textBrowser")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 570, 501, 20))
        self.textEdit.setObjectName("textEdit")
        
        self.inputbutton = QtWidgets.QPushButton(Form)
        self.inputbutton.setGeometry(QtCore.QRect(510, 570, 41, 23))
        self.inputbutton.setObjectName("inputbutton")
        self.to_user1 = QtWidgets.QPushButton(Form)
        self.to_user1.setGeometry(QtCore.QRect(560, 490, 40, 23))
        self.to_user1.setObjectName("to_user1")
        self.to_user2 = QtWidgets.QPushButton(Form)
        self.to_user2.setGeometry(QtCore.QRect(610, 490, 40, 23))
        self.to_user2.setObjectName("to_user2")
        self.to_user3 = QtWidgets.QPushButton(Form)
        self.to_user3.setGeometry(QtCore.QRect(660, 490, 40, 23))
        self.to_user3.setObjectName("to_user3")
        self.to_user4 = QtWidgets.QPushButton(Form)
        self.to_user4.setGeometry(QtCore.QRect(710, 490, 40, 23))
        self.to_user4.setObjectName("to_user4")
        self.to_user5 = QtWidgets.QPushButton(Form)
        self.to_user5.setGeometry(QtCore.QRect(560, 520, 40, 23))
        self.to_user5.setObjectName("to_user5")
        self.to_user6 = QtWidgets.QPushButton(Form)
        self.to_user6.setGeometry(QtCore.QRect(610, 520, 40, 23))
        self.to_user6.setObjectName("to_user6")
        self.to_user7 = QtWidgets.QPushButton(Form)
        self.to_user7.setGeometry(QtCore.QRect(660, 520, 40, 23))
        self.to_user7.setObjectName("to_user7")
        self.to_user8 = QtWidgets.QPushButton(Form)
        self.to_user8.setGeometry(QtCore.QRect(710, 520, 40, 23))
        self.to_user8.setObjectName("to_user8")
        self.Date = QtWidgets.QLabel(Form)
        self.Date.setGeometry(QtCore.QRect(10, 20, 56, 12))
        self.Date.setObjectName("Date")
        self.Timer = QtWidgets.QLabel(Form)
        self.Timer.setGeometry(QtCore.QRect(510, 20, 56, 12))
        self.Timer.setObjectName("Timer")
        self.myname = QtWidgets.QLabel(Form)
        self.myname.setGeometry(QtCore.QRect(620, 80, 80, 12))
        self.myname.setObjectName("myname")
        self.myjob_image = QtWidgets.QLabel(Form)
        self.myjob_image.setGeometry(QtCore.QRect(620, 220, 56, 12))
        self.myjob_image.setObjectName("myjob_image")
        self.output_info = QtWidgets.QLabel(Form)
        self.output_info.setGeometry(QtCore.QRect(560, 460, 60, 12))
        self.output_info.setObjectName("output_info")

        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inputbutton.setText(_translate("Form", "전송"))
        self.to_user1.setText(_translate("Form", "유저1"))
        self.to_user2.setText(_translate("Form", "유저2"))
        self.to_user3.setText(_translate("Form", "유저3"))
        self.to_user4.setText(_translate("Form", "유저4"))
        self.to_user5.setText(_translate("Form", "유저5"))
        self.to_user6.setText(_translate("Form", "유저6"))
        self.to_user7.setText(_translate("Form", "유저7"))
        self.to_user8.setText(_translate("Form", "유저8"))
        self.Date.setText(_translate("Form", "날짜"))
        self.Timer.setText(_translate("Form", "시간"))
        self.myname.setText(_translate("Form", "자기닉네임"))
        self.myjob_image.setText(_translate("Form", "직업사진"))
        self.output_info.setText(_translate("Form", "투표하세요"))
  
