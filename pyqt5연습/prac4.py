import sys
from tkinter import Menu
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction, QMenu,qApp
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("하이하이")

        menu = self.menuBar()       #메뉴 생성
        menu_file = menu.addMenu('File')    #메뉴 그룹 생성
        menu_edit = menu.addMenu('Edit')
        menu_view = menu.addMenu('View')


        file_exit = QAction('Exit',self)    #file에 대한 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 나가짐')

        file_exit.triggered.connect(qApp.quit) #액션 부여해주기
        

        new_txt = QAction('텍스트 파일',self)
        new_py = QAction('파이썬 파일',self)

        file_new = QMenu('New',self)    #파일 안에 서브 그룹

        file_new.addAction(new_txt) #서브 메뉴
        file_new.addAction(new_py)

        view_stat = QAction('상태표시줄',self,checkable = True)# menu_view 하위
        view_stat.setChecked(False)

        view_stat.triggered.connect(self.tglStat)


        menu_file.addMenu(file_new)  #메뉴 등록
        menu_file.addAction(file_exit)  #메뉴 액션등록

        menu_view.addAction(view_stat)

        self.resize(450,400)
        self.setWindowTitle('안이ㅏ나ㅣ이ㅏㄴ아ㅣ')
        self.show()
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
    def contextMenuEvent(self,QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")

        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        
        if action == quit:
            qApp.quit()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())