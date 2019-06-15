import socket, sys
from multiprocessing import Process


HOST_IP = '127.0.0.1'
SERVER_IP = '127.0.0.1'

HOST_PORT = 1235
SERVER_PORT = 1235


class Chat:
    def __init__(self, host_ip, server_ip, host_port, server_port):
        self.host_ip = host_ip
        self.server_ip = server_ip

        self.host_port = host_port
        self.server_port = server_port

        self.has_connection = False
        self.is_connected = False
        
        self.server_sock = socket.socket()
        self.client_sock = socket.socket()

        
    def attempt_connection(self):
        try:
            self.client_sock.connect((self.server_ip, self.server_port))
            self.is_connected == True
            print("You are now connected...")

        except Exception as e:
            print(e)
    def get_connection(self):
        self.server_sock.bind((self.host_ip, self.host_port))
        self.server_sock.listen(1)
        conn, client_addr = self.server_sock.accept()

        self.conn = conn

        self.has_connection = True
        

    def send_loop(self, connObj):
        '''
        Loop that takes input from user and
        writes that to the connection object representing the 
        corresponding socket.
        '''

        while True:
            message = input('-->')
            if message == '__exit':
                print('Closing connection and exiting the program...')
                connObj.close()
                sys.exit()
            if message == '':
                continue
            else:
                connObj.sendall(message.encode('UTF-8'))
            

    def read_loop(self, connObj):
        '''
        Loop that reads from the connection and
        displays the output for the user.
        '''

        while True:
            incoming_message = connObj.recv(2000)
            if incoming_message == '':
                continue
            else:
                print(str(incoming_message.decode('UTF-8')))
    
    def encrypt(self):
        pass


    def decrypt(self):
        pass


def process_wrapper(function):
    def wrapper(*args):
        p_function = Process(target=function, args=args)
        p_function.start()
    return wrapper


@process_wrapper
def connect(chat):
    get_connection = Process(target=chat.get_connection)
    
    attempt_connection = Process(target=chat.attempt_connection)
    

    get_connection.start()
    attempt_connection.start()

@process_wrapper
def read_and_write(chat, conn):
    send_loop = Process(target=chat.send_loop, args=(conn, ))
    read_loop = Process(target=chat.read_loop, args=(conn, ))


    send_loop.start()
    read_loop.start()


def main():
    chat = Chat(HOST_IP, SERVER_IP, HOST_PORT, SERVER_PORT)
    
    connect(chat)

  
if __name__ == '__main__':
    main()
