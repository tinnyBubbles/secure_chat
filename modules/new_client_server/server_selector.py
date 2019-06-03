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
    usrID = socketObj.gethostbyname()
    message_header = socketObj.recv(HEADER_LENGTH)
    message_length = int(message_header.decode("UTF-8").strip())
    message_data = socketObj.recv(message_length)
    message_text = message_data.decode("UTF-8")
    message = {usrID: (message_length, message_text)}
    return message


def send_message(socketObj, message_length, message_text):
    socketObj.sendall(message_header.encode("UTF-8") + message_data.encode("UTF-8"))


def record_conv(clients):
    pass


sel = selectors.DefaultSelector()
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(IP, PORT)
server_sock.listen()

while len(clients) < 2:
    client_sock, client_addr = server_sock.accept()
    clients.update({client_socket: client_addr})

    sel.register(client_sock, selectors.EVENT_READ, receive_message)

while True:

