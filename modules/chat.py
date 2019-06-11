import socket
from multiprocessing import Process
import sys

host = ('127.0.0.1', 1234)
client = ('127.0.0.1', 1234)




class Chat:
    class ProcessWrapper:
        def __init__(self, function):
            self.function = function
        
        def __call__(self, *arguments, **kwargs):
            self.p = Process(target=self.function, args=arguments)
            self.p.start()
            self.p.join()
            self.p.terminate()


    def __init__(self, chat_host, chat_client):
        self.ip, self.port = chat_host
        self.chat_client = chat_client
        self.is_connected = False
        
        self.chat_client = chat_client

       
    @ProcessWrapper
    def attempt_connection(self, client):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(False)
        s.connect(client)
        s.close()
        return True
    
    
    @ProcessWrapper
    def get_connection(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(False)
        s.bind((ip, port))
        s.listen()
        conn, addr = s.accept()

        s.close()
        return conn

    @ProcessWrapper
    def send_loop(conn, sock1, sock2):
        '''
        Loop that takes input from user and
        writes that to the connection object representing the 
        corresponding socket.
        '''
        while True:
            message = input('-->')
            if message == '__exit':
                print('Closing connection and exiting the program...')

                sock1.flush()
                sock1.close()
                sock2.flush()
                sock2.close()

                sys.exit()
            if message == '':
                continue
            else:
                conn.sendall(message.encode('UTF-8'))
            

    @ProcessWrapper
    def read_loop(conn):
        '''
        Loop that reads from the connection and
        displays the output for the user.
        '''
        while True:
            incoming_message = conn.recv(2000)
            if incoming_message == '':
                continue
            else:
                return incoming_message
    

    def run(self):
        response = input('Would you like to initiate a chat?[Y/N]')
        
        if response == 'Y':
            conn = self.get_connection(self.ip, self.port)
            while self.is_connected == False:
                self.is_connected = self.attempt_connection(self.chat_client)

            read_loop(conn)
            send_loop(conn, self.s, self.s2)

        if response == 'N':
            print('Exiting')
            sys.exit()

        else:
            print('Invalid response ... exiting')
            sys.exit()
        
    def encrypt(self):
        pass


    def decrypt(self):
        pass


if __name__ == '__main__':
    chat = Chat(host, client)
    chat.run()
    
