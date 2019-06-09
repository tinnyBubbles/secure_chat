import socket
import encrypt as e
import sys


IP = '127.0.0.1'
PORT = 1234


class client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def send(self, message):
        try:
            self.sock.send(message.encode('UTF-8'))
            return 1
        except Exception:
            return Exception

    def receive(self):
        try:
            message = self.sock.recv(2000)
            return message.decode('UTF-8') 
        except:
            return 0

    def connect(self, ip, port):
        try:
            self.sock.connect((ip, port))
            return 1
        except Exception:
            return Exception

    def encrypt(self):
        pass

    def decrypt(self):
        pass

client = client()

connection_status = client.connect(IP, PORT)

if connection_status == 1:
    print("Connected ...")

else:
    print(status_msg)
    sys.exit()
    
while True:

    message = input("-->")

    send_status = client.send(message)

    if send_status == 1:
        print("Message sent")

    else:
        print(send_status)
        sys.exit()
    
    receive_status = client.receive()

    if receive_status == 0:
        print("error")
    else:
        print(receive_status)

