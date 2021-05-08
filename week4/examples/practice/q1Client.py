'''
AUTHOR: SAGNIK CHATTERJEE
Write a program where client can send a message to the server and the server can receive
the message and send, or echo, it back to the client.
'''
import socket 
HOST = "127.0.0.1"
PORT= 9000 
with socket.socket(socket.AF_INET ,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello all,this is a random message')
    data = s.recv(3000)
    print("Received Connection... ",end="\n")
    print(f"Server data sent is  : {data.decode()}")


