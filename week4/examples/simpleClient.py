import socket

host = socket.gethostname()
port = 12345
s = socket.socket()
s.connect((host, port))
s.sendall(b'Welcome user, this message indicates it works ')
data = s.recv(1024)
s.close()
print(repr(data))
