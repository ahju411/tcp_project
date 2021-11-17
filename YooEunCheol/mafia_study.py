import time
import threading

def func1():
    global flag
    flag = threading.Event()
    while not flag.is_set():
        for i in range(0,50):
            time.sleep(0.2)
    print("func1 die")

def func2():
    total=0
    for i in range(0,30) :
        total += i
        time.sleep(0.5)
        if total >= 55 :
            print("func2 die")
            return 1

t1=threading.Thread(target=func1)
t2=threading.Thread(target=func2)
t1.daemon=True
t2.daemon=True

t1.start()
t2.start()
t2.join()
flag.set()
t1.join()

print("exit") #input()