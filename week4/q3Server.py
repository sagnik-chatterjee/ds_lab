"""
AUTHOR: SAGNIK CHATTERJEE

Write a TCP/UDP peer to peer chat system between two different machines.

"""

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT  = 8000 # Port to listen on (non-privileged ports are > 1023)

s = socket.socket()
s.bind((HOST, PORT))
s.listen()

print(f"Peer To Peer Chat Server started at port := {PORT}\n")
conn, addr = s.accept()

print(f"Received connection from host:= {addr[0]} ,port:=  {addr[1]} \n")
s_name = conn.recv(1024)
s_name = s_name.decode()

print(s_name, "has connected to the chat room\nEnter F to exit chat room\n")
name = input(str("Enter your name: "))
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "F":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
    break

conn.send(message.encode())
message = conn.recv(1024)
message = message.decode()
print(s_name, ":", message)
