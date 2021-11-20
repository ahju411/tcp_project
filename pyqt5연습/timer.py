import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.setWindowTitle('QTimer')
        self.setGeometry(100, 100, 600, 280)
 
        layout = QVBoxLayout()
 
        self.lcd = QLCDNumber()
        self.lcd.display('')
        self.lcd.setDigitCount(8)
        subLayout = QHBoxLayout()
        
        self.btnStart = QPushButton("시작")
        self.btnStart.clicked.connect(self.onStartButtonClicked)
 
        self.btnStop = QPushButton("멈춤")
        self.btnStop.clicked.connect(self.onStopButtonClicked)
 
        layout.addWidget(self.lcd)
        
        subLayout.addWidget(self.btnStart)
        subLayout.addWidget(self.btnStop)
        layout.addLayout(subLayout)
 
        self.btnStop.setEnabled(False)
        self.setLayout(layout)        
    def onStartButtonClicked(self):
        self.timer.start()
        self.btnStop.setEnabled(True)
        self.btnStart.setEnabled(False)
    def onStopButtonClicked(self):
        self.timer.stop()
        self.btnStop.setEnabled(False)
        self.btnStart.setEnabled(True)
    def timeout(self):
        sender = self.sender()
        m = 5
        s = 50
        currentTime = QTime.currentTime().toString("hh:mm:ss")
        minute = QTime(0,m,s).toString("hh:mm:ss")
        if id(sender) == id(self.timer):
            self.lcd.display(minute)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())