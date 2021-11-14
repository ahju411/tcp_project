# -*- coding: utf-8 -*-

import sys

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from automatic_writter import Ui_MainWindow #앞의 파일명 동일 kinwriter_python 만 변경
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import pyperclip
from bs4 import BeautifulSoup
import pyautogui
import os

class auto_w(QMainWindow,Ui_MainWindow): #class name 변경
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()
    def program_start(self):
        driver = webdriver.Chrome()
        driver.get("https://www.naver.com")
        
    def program_stop(self):
        qApp.exit()
os.getcwd()
app =QApplication([])
main_dialog = auto_w() #해당부분 위 class name과 동일하게 작성
QApplication.processEvents()
app.exit(app.exec_())