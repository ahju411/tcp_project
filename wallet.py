class mywallet:
    print("로또 판매처에 오신걸 환영합니다")
    balance = 0
    haslotto = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        mywallet.balance = balance
        print('현재 {}님의 잔고는 {}원 입니다.'.format(name,mywallet.balance))
    def deposit(self,amount):
        if amount >= 1:
            mywallet.balance += amount
    def buylotto(self):
        print(mywallet.balance)
        print("로또를 몇개 구매하시겠습니까?")
        while(1):
            choice = int(input('개수'))
            if mywallet.balance >= 5000:
                if(mywallet.balance - int(choice * 5000) < 0 ):
                    print('무리하지마세요...')
                    continue
                mywallet.balance -= int(choice * 5000)
                print("로또를 {}개 구매하셨습니다.".format(choice))
                print('남은 잔액은 {}원입니다.'.format(mywallet.balance))
                mywallet.haslotto += choice
            elif mywallet.balance < 5000:
                print("잔액이 부족합니다.")
                break
    def info(self):
        print("{}님의 잔고는 {}원이며 현재 로또는 {}개 보유중입니다.".format(self.name,mywallet.balance,mywallet.haslotto))
kim = mywallet("혜성",10000)
kim.deposit(5000)
kim.buylotto()
kim.info()


