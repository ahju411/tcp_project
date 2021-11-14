# 메뉴
from tkinter import *

root = Tk()
root.title("메모장")
root.geometry("640x480") #가로 * 세로

menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File")
menu_file.add_command(label="Open File...")

menu.add_cascade(label="File", menu=menu_file)

root.config(menu=menu)
root.mainloop()

