import socket
import selectors


HEADER_LENGTH = 10
IP_ADDR = "127.0.0.1"
PORT = 1234

write_sockets = []
read_sockets = []
error_sockets = []
clients = {}

def receive_message(socketObj):
    message_header = socketObj.recv(HEADER_LENGTH)
    message_length = int(message_header.decode("UTF-8"))
    message_data = socketObj.recv(message_length)
    return message(message_header, message_data)


def send_message(socketObj, message_header, message_data):
    socketObj.sendall(message_header.encode("UTF-8") + message_data.encode("UTF-8"))


def record_conv(clients):
    pass
