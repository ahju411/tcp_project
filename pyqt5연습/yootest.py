import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("tcp_project\pyqt5연습\MainWindow - untitled.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()