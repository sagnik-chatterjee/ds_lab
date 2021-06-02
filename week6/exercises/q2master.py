import socket
import datetime
import time


def initiate_clock_server():
    s = socket.sokcet()
    print("Socket creation successfull")

    port = 8011
    s.bind(("", port))
    s.listen(5)
    print("Socket started listening :> ")
    while True:
        connection, address = s.accept()
        print("Server COnnected to ", address)
        connection.send(str(datetime.datetime.now()).encode())


if __name__ == '__main__':
    initiate_clock_server()
