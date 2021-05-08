# echo server program
import socket

host = socket.gethostname()
port = 12345
s = socket.socket()
s.bind((host, port))
s.listen(5)
print(f"Started the simple server , at port := {port}")
conn, addr = s.accept()
print(f"Got connection from   {addr[0]} , {addr[1]}")
print("Thanks for connecting ")
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
