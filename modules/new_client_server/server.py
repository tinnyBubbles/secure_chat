"""
    Objects:
        Read socket
        Write socket
        Selector for monitoring socket object events
    Functions:
        Create socket
        Read from a socket
        Write to a socket
        Log actions and errors
    Containers:
        HEADER_LENGTH
        IP_ADDR
        PORT
        Client_Dictionary
        SocketsReadyToWrite
        SocketsReadyToRead
"""

import socket
import select

#Setting a fixed header length
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

#Creating a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Using setsockopt method to set options on the socket wich allow us to reuse the socket after each connection
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

#Creating a list to store current socket objects
sockets_list = [server_socket]

#Creating a dictionary that keeps the client object paired with the data it has
clients = {}


def receive_message(client_socket):
    """
    Receives the message header and length of the client_socket passed in as the argument.
    Returns a dictionary with the keys 'header' and 'data'; and the values message_header and the 
    message from the client_socket respectively. 
    """
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False


#Begin reading incoming connections and messages
while True:
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_addr = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print("Accepted new connection from:" + client_addr)
        else:
            message = receive_message(notified_socket)

            if message is False:
                print("Closed connection from:" + notified_socket.gethostbyname())
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            user = clients[notified_socket]
            print("Received message from:" + notified_socket.gethostbyname())

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['data'])
