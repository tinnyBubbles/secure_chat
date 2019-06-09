import socket
import selectors


IP_ADDR = '127.0.0.1'
PORT = 1234

clients = {}

def get_connections(sockObj, selectorObj, dictConn):
    while len(dictConn) < 2:
        conn, addr = sockObj.accept()
        dictConn.update({conn: addr})
        selectorObj.register(conn, selectors.EVENT_READ)


def relay_messages(selectorObj, dictConn):
    while True:
        read_sockets = selectorObj.select()

        for ready_socket, event in read_sockets:
            conn = ready_socket.fileobj
            message = conn.recv(2000)
            for conn in dictConn:
                if conn == conn:
                    continue
                else:
                    conn.send(message)


sel = selectors.DefaultSelector()
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind((IP_ADDR, PORT))
server_sock.listen(2)

get_connections(server_sock, sel, clients)

relay_messages(sel, clients)


