import socket 
import datetime 
import time 


def initiate_clock_server():
    s=socket.socket()
    print("Socket was successfullyy created")
    port =8011
    s.bind("",port)
    s.listen(5)
    print("Socket is listening")

    while True:
        connection ,address = s.accept()
        print(f"Server connected to {address}")
        connection.send(str(datetime.datetime.now()).encode())

if __name__=='__main__':
    initiate_clock_server()
