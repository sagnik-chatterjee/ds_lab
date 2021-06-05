import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer


def synchronizeTime(device_type):

    s = socket.socket()

    port = 8011

    s.connect(("127.0.0.1", port))

    request_time = timer()

    server_time = parser.parse(s.recv(1024).decode())
    response_time = timer()
    actual_time = datetime.datetime.now()
    print(f" :|> Synchronising now :- {device_type}")
    print(f" :|> Time returned by server: {server_time} ")

    process_delay_latency = response_time - request_time

    print(f" :|> Process Delay latency: {process_delay_latency}  seconds")

    print(f" :|> Actual clock time at client side: {actual_time}")

    client_time = server_time + datetime.timedelta(seconds=(process_delay_latency) / 2)

    print(f" :|> Synchronized process client time: {client_time}")

    error = actual_time - client_time
    print(f" :|> Synchronization error : {error.total_seconds()} seconds.")
    s.close()


if __name__ == "__main__":

    synchronizeTime("LAPTOP")