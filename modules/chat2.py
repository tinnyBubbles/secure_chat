import socket, sys
from multiprocessing import Process



class Chat:
    def __init__(self, server_ip, server_port, host_ip, host_port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  
        self.server_ip = server_ip
        self.server_port = server_port

        self.host_ip = host_ip
        self.host_port = host_port

        self.sock.settimeout(20)
    
    def connect(self):
        try:
            self.sock.connect((self.server_ip, self.server_port))
            print("You are now connected ...")
            return True, self.sock
        except:
            print("Could not connect ...")
            return False
    
    
    def accept_conn(self):
        try:
            print("Listening ...")
            self.sock.bind((self.host_ip, self.host_port))
            self.sock.listen()
            return self.sock.accept()
            print("Accepted a connection")
            self.sock.close()
        except:
            print("Could not receive a connection ... exiting")
            sys.exit()


    def send(msg, sock):
        sock.send(msg.encode('UTF-8'))
        

    def receive(sock):
        incoming_msg = sock.recv(2000)
        return incoming_msg.decode('UTF-8')

class Logger:
    pass


class Monitor:
    pass


class UI:
    pass


class Cipher:
    pass


def main():
    chat_client = Client(s, SERVER_IP, SERVER_PORT)

    is_connected, s = chat_client.connect()
    
    if is_connected == True:
        #send and receive messages on seperate processes

    elif is_connected == False:
        chat_server = Server(s, HOST_IP, HOST_PORT)
        conn, addr = chat_server.accept_conn()
    else:
        print("Something went wrong. Exiting")
        sys.exit()

