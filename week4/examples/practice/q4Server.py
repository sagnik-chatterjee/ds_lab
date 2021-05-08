import socket
import os
from _thread import *

server_socket = socket.socket()
host = "127.0.0.1"
port = 11596
thread_count = 0
try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waiting for a connection:")
server_socket.listen(5)


def thread_client(connection):
    connection.send(str.encode("Welcome to the Server"))
    while True:
        data = connection.recv(2048)#max upto 2048 bytes receive
        print(f"Received from client: {str(thread_count)} ,{data.decode()}")

        inputs = input("Server Says:")
        if not data:
            break
        connection.sendall(inputs.encode())
    connection.close()


while True:
    client, address = server_socket.accept()
    print(f"Connected To: {address[0]} : {str(address[1])}")
    start_new_thread(thread_client, (client,))
    thread_count += 1
    print(f"Thread NUmber: {str(thread_count)}")
server_socket.close()
