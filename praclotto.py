import cx_Oracle
import random
class lotto:
    compare = 0
    bonus = 0
    def startlotto():
        user = []
        while len(user) < 6:
            try:
                value = int(input("{}번 째 로또 번호를 입력해주세요.".format(len(user)+1)))
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
        elif lotto.compare == 4:
            print("5만원 10배 이득 보셨습니다~")
        elif lotto.compare == 5:
            print("아쉽게 3등이네요")
        elif lotto.compare == 5 and lotto.bonus == 1:
            print("2등입니다..엄청난 행운아네요")
        elif lotto.compare == 6:
            print("1등입니다 당신은 신인가요?")

        
lotto.startlotto()
lotto.calculate()