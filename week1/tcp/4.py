import socket

HOST = "172.16.58.37"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b"hello world!from sagnik")
	data = s.recv(1024)
	print("recvd", data)