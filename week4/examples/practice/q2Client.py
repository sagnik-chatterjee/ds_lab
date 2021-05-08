"""
Author: Sagnik Chatterjee
Write a program to create TCP time server in Python
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object ,tcp type

host = socket.gethostname() #local macchine name
port = 9456

print("Client  Working   ")
s.connect((host, port)) #connect 

tm = s.recv(1024)
print(" Current time from Server Received is  :", tm.decode())
s.close()
