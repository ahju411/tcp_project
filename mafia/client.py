import socket
import threading

def Send(client_sock):
    #global nickname 
    #nickname= input('닉네임을 입력하세요: ')
    #client_sock.send(nickname.encode('utf-8'))
    while True:
        send_data = input()
        client_sock.send(send_data.encode('utf-8'))
       # print(send_data)
        if send_data == '/q':
            print('연결 종료')
            client_sock.close()

def Recv(client_sock,user):
    while 1:
        try:
            recv_data = client_sock.recv(1024).decode()
            
        except:
            print('연결끊김')
            break
       
        if not user in recv_data:
           # print('실행되냐')
            print(recv_data)

if __name__=='__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
    Host = '118.217.168.174' #192.168.35.245 118.217.168.174
    Port = 9000
    client_sock.connect((Host,Port))
>>>>>>> 0c9852769702e324459d4233f5c1ce96cf78f569
    print('Connecting to',Host,Port)

    thread2 = threading.Thread(target=Recv, args=(client_sock,user))
   # thread2.daemon = True
    thread2.start()

    thread1 = threading.Thread(target=Send,args=(client_sock,))
   # thread1.daemon=True
    thread1.start()
