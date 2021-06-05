from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time


def startSendingTime(name, slave_client):

    while True:

        slave_client.send(str(datetime.datetime.now()).encode())

        print(f" :|> Recent time sent successfully by {name}", end="\n\n")
        time.sleep(5)


def startReceivingTime(name, slave_client):

    while True:

        Synchronized_time = parser.parse(slave_client.recv(1024).decode())

        print(
            f" :|> Synchronized time at the client is {name} : {str(Synchronized_time)}",
            end="\n",
        )


def initiateSlaveClient(name, port=8080):

    slave_client = socket.socket()

    slave_client.connect(("127.0.0.1", port))

    print("Starting to receive time from server\n")
    send_time_thread = threading.Thread(
        target=startSendingTime, args=(name, slave_client)
    )
    send_time_thread.start()

    print(f" :|> Starting to recieving synchronized time from server\n")
    receive_time_thread = threading.Thread(
        target=startReceivingTime, args=(name, slave_client)
    )
    receive_time_thread.start()


if __name__ == "__main__":

    client = "SOLS"
    initiateSlaveClient(client, port=8080)
