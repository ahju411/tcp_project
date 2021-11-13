a = 3
print(a * 3)
b = 133
print( a + b)
class student:
    def __init__(self,name,id):
        print("hi{0} your id is {1}".format(name,id))
st =  student('홍길동','1234')
class MenuClass:
    menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
    price = [0,1500, 2000, 1700, 2500, 2000, 1900]
    bill = [0, 10000, 5000, 1000]
    #############################
    # 메뉴 보이기
    def menu_print(self):
        i = 1
        while i< len(self.menu):
            print(i, self.menu[i], self.price[i])
            i = i+1    
menu = MenuClass()
menu.menu_print()