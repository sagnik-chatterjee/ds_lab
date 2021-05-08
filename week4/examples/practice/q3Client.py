"""
AUTHOR: SAGNIK CHATTERJEE
Write a TCP chat server in python using socket programming.
"""

import socket

HOST = "127.0.0.1"
PORT = 31621

s = socket.socket()
name = input(str("Enter name  :  "))
print(f"Trying to connect to  := {HOST} , := {PORT}", end="\n")

s.connect((HOST, PORT))
print("Connected...", end="\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(f"{s_name} has joined the chat room \n Enter F,  to exit chat room", end="\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "F":
        message = f"{s_name} Left chat room! , "
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
