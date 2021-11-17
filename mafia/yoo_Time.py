


i=10
def startTimer():
    global i
    print(i)
    i-=1
    timer = threading.Timer(1,startTimer)
    timer.start()
    if i==0 :
        timer.cancel()
        return i
    