import socket

HOST = "172.16.58.37"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print("connected by:", addr)
		while 1:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)