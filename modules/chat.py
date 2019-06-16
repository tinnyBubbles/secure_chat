import socket, sys, selectors
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

        self.sel = selectors.DefaultSelector()
        
        self.server_sock = socket.socket()
        self.client_sock = socket.socket()

        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
        self.client_sock.setblocking(True)
        self.server_sock.setblocking(True)

    def attempt_connection(self):
        try:
            self.client_sock.connect((self.server_ip, self.server_port))
            self.is_connected = True
            peer_name = self.client_sock.getpeername()
            print("You are now connected... " + str(peer_name))

        except Exception as e:
            print(e)
    def get_connection(self):
        self.server_sock.bind((self.host_ip, self.host_port))
        self.server_sock.listen(1)
        self.conn, self.client_addr = self.server_sock.accept()
        
        print(str(client_addr) + " " + "has now connected...")
    
    def read(self):
        while True:
            self.incoming_message = self.conn.recv(2000)
            if incoming_message == '':
                continue
            else:
                print(str(self.incoming_message.decode('UTF-8')))
    
    
    def send(self):
         while True:
             self.message = input('-->')
             if self.message == '__exit':
                print('Closing connection and exiting the program...')
                sys.exit()
             if self.message == '':
                continue
             else:
                self.client_sock.sendall(self.message.encode('UTF-8'))
        
        #self.sel.register(conn, selectors.EVENT_READ)
        #self.sel.register(conn, selectors.EVENT_WRITE)
        
        #event = sel.select()

        #self.has_connection = True
        #use selectors to listen for read and write events
   
    def encrypt(self):
        pass


    def decrypt(self):
        pass


def process_decorator(to_wait=False):
    def process_wrapper(function):
        def wrapper(*args):
            p_function = Process(target=function, args=args)

            if to_wait==False:
                p_function.start()
            if to_wait==True:
                p_function.start()
                p_function.join()
            else:
                p_function.start()
        return wrapper
    return process_wrapper


@process_decorator(to_wait=True)
def connect(chat):
    get_connection = Process(target=chat.get_connection)
    
    attempt_connection = Process(target=chat.attempt_connection)
    

    get_connection.start()
    
    attempt_connection.start()

@process_decorator(to_wait=True)
def read_and_write(chat):
    send_loop = Process(target=chat.send)
    read_loop = Process(target=chat.read)


    send_loop.start()
    read_loop.start()


def main():
    chat = Chat(HOST_IP, SERVER_IP, HOST_PORT, SERVER_PORT)
    
    connect(chat)
    
    read_and_write(chat)

    print(str(chat.has_connection))
    print(str(chat.is_connected)) 
if __name__ == '__main__':
    main()
