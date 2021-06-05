import socket
import datetime
import time


def initiateClockServer():
    s = socket.socket()
    print(" :|> Socket successfully created")

    port = 8011
    s.bind(("", port))

    s.listen(5)
    print(":|> Socket is listening")

    while True:
        connection, address = s.accept()
        print(f" :|> Server connected to {address}")
        connection.send(str(datetime.datetime.now()).encode())


if __name__ == "__main__":

    initiateClockServer()
