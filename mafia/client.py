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
    Host = '192.168.35.245'
    Port = 9090
    user = input('닉네임: ')
    client_sock.connect((Host,Port))
    client_sock.send(user.encode('utf-8'))
    print('Connecting to',Host,Port)

    thread2 = threading.Thread(target=Recv, args=(client_sock,user))
   # thread2.daemon = True
    thread2.start()

    thread1 = threading.Thread(target=Send,args=(client_sock,))
   # thread1.daemon=True
    thread1.start()
