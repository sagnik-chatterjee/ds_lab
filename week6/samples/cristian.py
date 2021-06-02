import socket 
import datetime 
import time 


def initialClockServer():
    s =socket.socket()
    port =8000
    s.bind((port))
    s.listen(10)
    print("Scoket now listening")
    while True:
        connection,address =s.accept()
        print("Server connected to ",address)
    
        #respond the clinet with server clok time 
        connection.send(str(datetime.datetime.now()).encode())
        connection.close()

initialClockServer()