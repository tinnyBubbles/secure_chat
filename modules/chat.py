import socket
from multiprocessing import Process
import sys

#HOST = ('127.0.0.1', 1234)
#SERVER = ('127.0.0.1', 1234)

HOST_IP = '127.0.0.1'
SERVER_IP = '127.0.0.1'

HOST_PORT = 1235
SERVER_PORT = 1235


class Chat:
    class Decorators:
        @classmethod
        def processwrapper(funcInstance, function):
            def wrapper(*arguments):
                p = Process(target=function, args=arguments) 
                p.start()

            return wrapper


    def __init__(self, host_ip, server_ip, host_port, server_port):
        self.host_ip = host_ip
        self.server_ip = server_ip

        self.host_port = host_port
        self.server_port = server_port

        self.has_connection = False
        self.is_connected = False
        
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)


    def connect(self):
        while self.is_connected == False and self.has_connection == False:
            self.get_connection(self.host_ip, self.host_port)
            self.attempt_connection()
        return True

    #@Decorators.processwrapper    
    def attempt_connection(self):
        #adjust to keep trying to connect until connection is success
        #self.s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.setblocking(False)
        self.sock.connect((self.server_ip, self.server_port))
        
        self.is_connected = True
    
    #@Decorators.processwrapper 
    def get_connection(self, host_ip, host_port):
        #s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        self.sock.bind((host_ip, host_port))
        self.sock.listen(1)
        conn, client_addr = self.sock.accept()
        self.connection = conn
        self.client_addr = client_addr
    
        
        self.has_connection = True

    
    def send_loop(self):
        '''
        Loop that takes input from user and
        writes that to the connection object representing the 
        corresponding socket.
        '''
        while True:
            message = input('-->')
            if message == '__exit':
                print('Closing connection and exiting the program...')
                self.connection.close()
                sys.exit()
            if message == '':
                continue
            else:
                self.connection.sendall(message.encode('UTF-8'))
            

    def read_loop(self):
        '''
        Loop that reads from the connection and
        displays the output for the user.
        '''
        while True:
            incoming_message = self.connection.recv(2000)
            if incoming_message == '':
                continue
            else:
                print(str(incoming_message.decode('UTF-8')))
    def run_on_process(self, processObj, method):
        pass

    def encrypt(self):
        pass


    def decrypt(self):
        pass


def main():
    chat = Chat(HOST_IP, SERVER_IP, HOST_PORT, SERVER_PORT)
    
    p1 = Process(target=chat.connect)
    p1.start()


    chat.read_loop()
    chat.send_loop()
    
if __name__ == '__main__':
    main()
