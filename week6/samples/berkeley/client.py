from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time


def start_sending_time(slave_client):
    while True:
        slave_client.send(str(datetime.datetime.now()).encode())
        print("Recent time sent successfully")
        time.sleep(5)


def start_receiving_time(slave_client):
    while True:
        sync_time = parser.parse(slave_client.recv(1024).decode())
        print(f"Sync time at the client is {sync_time}")


def initiate_slave_client(port=8080):
    slave_client = socket.socket()
    slave_client.connect(("127.0.0.1", port))

    print("Starting to  receive time from server\n")
    send_time_thread = threading.Thread(target=start_sending_time, args=(slave_client,))
    send_time_thread.start()

    print(f"Starting  to receive sync time from server")
    receive_time_thread = threading.Thread(
        target=start_receiving_time, args=(slave_client,)
    )
    receive_time_thread.start()


if __name__ == "__main__":
    initiate_slave_client(port=8080)
