import socket

PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((socket.gethostname(), PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(b'Data received')
			
