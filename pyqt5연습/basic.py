import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())