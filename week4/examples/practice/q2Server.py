'''
Author: Sagnik Chatterjee
Write a program to create TCP time server in Python
'''

import socket 
import time 

#socket object creation 
serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9456

# bind to the port
serversocket.bind((host, port))

serversocket.listen(5) #queue 5 requests 

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print(f"Got a connection from    {str(addr)}")
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()