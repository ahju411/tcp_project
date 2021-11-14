import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget,QLabel,QGridLayout

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        
        # grid = QGridLayout()
        # self.setLayout(grid)

        # names = ['cls','bck','','Close',
        #         '7','8','9','/',
        #         '4','5','6','*'
        #         ,'1','2','3','-'
        #         ,'0','.','=','+']
        # positions = [(i,j) for i in range(5) for j in range(4)] #i가 0~4까지 돌때 j가 0~3까지 도는거 i가 0일때 j가 0 1 2 3 이런 식 
        # for position, name in zip(positions,names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position) #*은 (0,1)뭐 이런 식이 아니라 0하고 1 이렇게 넘기게 해주는거다 button,0,1 이런식으로 계속 넘기는거임 
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,10,1)

       

        self.setLayout(grid)

        self.move(300,150)
        self.setWindowTitle('하이하이')
        self.show()
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())