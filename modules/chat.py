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
        conn, client_addr = self.server_sock.accept()
        
        print(str(client_addr) + " " + "has now connected...")
        #self.conn = conn
        
        self.sel.register(conn, selectors.EVENT_READ)
        self.sel.register(conn, selectors.EVENT_WRITE)
        
        event = sel.select()

        #self.has_connection = True
        #use selectors to listen for read and write events
        #then take appropriate action with conn
        """
            -initialize with a selector object unique to instance
            -register conn socket object returned by accept()
            -wait for conn socket object to have either a read or a write event.
            -if read event: then read and print to user
            -if write event: then write to socket object
            -repeat
        """
        
        for key, mask in event:
            if mask == 
        while True:
                message = input('-->')
                if message == '__exit':
                    print('Closing connection and exiting the program...')
                    conn.close()
                    sys.exit()
                if message == '':
                    continue
                else:
                    conn.sendall(message.encode('UTF-8'))
                

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
def read_and_write(chat, conn):
    send_loop = Process(target=chat.send_loop, args=(conn, ))
    read_loop = Process(target=chat.read_loop, args=(conn, ))


    send_loop.start()
    read_loop.start()


def main():
    chat = Chat(HOST_IP, SERVER_IP, HOST_PORT, SERVER_PORT)
    
    connect(chat)
    
    #read_and_write(chat, chat.conn)

    print(str(chat.has_connection))
    print(str(chat.is_connected)) 
if __name__ == '__main__':
    main()
