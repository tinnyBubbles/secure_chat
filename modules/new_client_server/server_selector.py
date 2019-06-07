import socket
import selectors
from collections import namedtuple

HEADER_LENGTH = 10
IP_ADDR = "127.0.0.1"
PORT = 1234

ClientKey = namedtuple('ClientKey', ['msgLength', 'msgData'])
Clients = {}

def receive_message(socketObj):
    message_header = socketObj.recv(HEADER_LENGTH)
    message_length = message_header.decode("UTF-8")

    message_data = socketObj.recv(int(message_length))

    key = ClientKey(message_length, message_data)

    return key


def send_message(socketObj, msgHeader, msgData):
    socketObj.sendall(msgHeader + message_data)


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
    Clients.update({conn: addr})

    sel.register(conn, selectors.EVENT_READ, receive_message)

while True:
    read_sockets = sel.select()
    for key, event in read_sockets:
        read_msg = key.data
        sock = key.fileobj
        clientKey = read_msg(sock)
        for client in Clients:
            if client == sock:
                continue
            else:
                send_message(client, clientKey.message_length, clientKey.message_data)  


