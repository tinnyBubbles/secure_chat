import socket
import selectors
from collections import namedtuple

HEADER_LENGTH = 10
IP_ADDR = "127.0.0.1"
PORT = 1234

ClientKey = namedtuple('ClientKey', ['msgLength', 'msgData'])
clients = {}

def receive_message(client_conn):

    message_data = client_conn.recv(2000)
    
    return message_data


def send_message(client_conn, message):
    client_conn.sendall(message)


def record_conv(clients):
    pass


sel = selectors.DefaultSelector()
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind((IP_ADDR, PORT))
server_sock.listen(2)

#Entering this loop because I only want 2 clients to be able to connect
#I also don't want to read or write to sockets until 2 and only 2 clients
#have been connected.

while len(Clients) < 2: 
    conn, addr = server_sock.accept()
    clients.update({conn: addr})

    sel.register(conn, selectors.EVENT_READ, receive_message)

while True:
    read_sockets = sel.select()
    for ready_socket in read_sockets:
        read_msg = ready_socket.data
        sock = ready_socket.fileobj
        message = receive_message(sock)
        for client in clients:
            if client[client_conn] == sock:
                continue
            else:
                send_message(client, message)  


