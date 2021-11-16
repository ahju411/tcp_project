import socket
import threading

def Send(client_sock):
    while True:
        send_data = bytes(input('내 닉네임: ').encode())
        client_sock.send(send_data)

def Recv(client_sock):
    while True:
        recv_data = client_sock.recv(1024).decode()
        print(recv_data)

if __name__=='__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = '118.217.168.174' #192.168.35.245 118.217.168.174
    Port = 9000
    client_sock.connect((Host,Port))
    print('Connecting to',Host,Port)

    thread1 = threading.Thread(target=Send,args=(client_sock,))
    thread1.start()

    thread2 = threading.Thread(target=Recv, args=(client_sock,))
    thread2.start()