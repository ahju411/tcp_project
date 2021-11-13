#import cx_Oracle
import random
class lotto:
    winmoney = 0
    compare = 0
    bonus = 0
    def startlotto():
        user = []
        lotto.compare = 0
        while len(user) < 6:
            try:
                value = int(input("{} 번째 로또 번호를 입력해주세요.".format(len(user)+1)))
            except:
                print("올바른 번호를 입력해주셔야죠. 다시 기회를 드릴게요")
                continue
            if value > 45:
                print("45 넘는건 로또 번호에 없어요. 다시")
                continue
            elif value < 1:
                print("1미만은 그냥 돈 버리는거죠. 다시")
                continue
            elif value in user:
                print("이미 있는 번호입니다. 다시하세요")
                continue
            user.append(int(value))
            user.sort()
        print("내가 뽑은 번호는 {}입니다.".format(user))
        computer = []
        while len(computer) < 7:
            value = random.randint(1,45)
            if value in computer:
                continue
            else:
                computer.append(value)
        computer.sort()
        for i in range(0,len(user)):
            if user[i] in computer[:6]:
                lotto.compare += 1
            elif user[i] == computer[6]:
                lotto.bonus += 1
        print("컴퓨터가 뽑은 로또 번호는 {}이고 보너스 번호는[{}]입니다.".format(computer[:6],computer[6]))
        print("당신은 {}개의 로또 번호를 맞췄습니다".format(lotto.compare))
        if lotto.bonus == 1:
            print("보너스 번호를 맞추셨습니다")
        
    def calculate():
        if lotto.compare < 3 :
            print("가져갈게 없네요..")
        elif lotto.compare == 3:
            print("5000원을 가져가세요~")
            lotto.winmoney += 5000
        elif lotto.compare == 4:
            print("5만원 10배 이득 보셨습니다~")
            lotto.winmoney += 50000
        elif lotto.compare == 5:
            print("아쉽게 3등이네요")
            lotto.winmoney += 2500000
        elif lotto.compare == 5 and lotto.bonus == 1:
            print("2등입니다..엄청난 행운아네요")
            lotto.winmoney += 50000000
        elif lotto.compare == 6:
            print("1등입니다 당신은 신인가요?")
            lotto.winmoney += 500000000

      
#lotto.startlotto()
#lotto.calculate()

class mywallet:
    print('-------------------------------')
    print("로또 판매처에 오신걸 환영합니다")
    print('-------------------------------')
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
        print('잔액:{}원'.format(mywallet.balance))
    def buylotto(self):
        print('잔액 {}원'.format(mywallet.balance))
        print("로또를 몇개 구매하시겠습니까?" )
        flag = True
        while(flag):
            choice = int(input('개수: '))
            if mywallet.balance >= 5000:
                if(mywallet.balance - int(choice * 5000) < 0 ):
                    print('무리하지마세요...')
                    continue
                mywallet.balance -= int(choice * 5000)
                print("로또를 {}개 구매하셨습니다.".format(choice))
                print('남은 잔액은 {}원입니다.'.format(mywallet.balance))
                if mywallet.balance <= 5000:
                    mywallet.haslotto += choice
                    break
                mywallet.haslotto += choice
                break
            elif mywallet.balance < 5000:
                print("잔액이 부족합니다. 돈을 충전하고 와주세요")
                break
    def info(self):
        print("{}님의 잔고는 {}원이며 현재 로또는 {}개 보유중입니다.".format(self.name,mywallet.balance,mywallet.haslotto))

name = input('이름을 입력해주세요: ')
money = int(input('잔고를 입력해주세요: '))
user1 = mywallet(name,money)
while(1):
    case = int(input('1.입금 2.구매 3.정보 4.나가기 --------' ))
    if case == 1:
        depositmoney = int(input('입글하실 돈을 입력해주세요: ' ))
        user1.deposit(depositmoney)
    elif case == 2:
        user1.buylotto()
    elif case == 3:
        user1.info()
    elif case == 4:
        print('이용해주셔서 감사합니다.')
        break
    else:
        print('잘못 입력하셨습니다')
        continue
if user1.haslotto == 0:
    print('로또를 구매하지 않아 참여할 수 없네요.')
else:
    print('로또 번호 추첨을 시작하겠습니다. 당신은 총 {}번 할 수 있습니다.'.format(user1.haslotto))
    while(user1.haslotto) > 0:
        lotto.startlotto()

        lotto.calculate()
        user1.haslotto -= 1

    print('총 {}원의 당첨금을 획득하였습니다.'.format(lotto.winmoney))
