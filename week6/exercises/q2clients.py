from os import sync
import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer


def synchronize_time(device_type):
    s = socket.socket()
    port = 8011
    s.connect(("127.0.0.1", port))
    request_time = timer()
    server_time = parser.parse(s.recv(1024).decode())
    response_time = timer()
    actual_time = datetime.datetime.now()
    print(f"Synchronizing {device_type}")
    print(f"Time returend by server:- {str(server_time)}")

    process_delay_latency = response_time - request_time
    print(f"Process Delay Latency: {str(process_delay_latency)} seconds")
    print(f"Actual Clock time at client side : {str(actual_time)}")
    client_time = server_time + \
        datetime.timedelta(seconds=(process_delay_latency)/2)

    print(f"Synchronized Process CLient time : {str(client_time)}")

    error = actual_time - client_time
    print(f"Synchronization error : {str(error.total_seconds())} seconds")
    print("Done")
    s.close()


if __name__ == '__main__':
    synchronize_time("DEVICE-1")
    synchronize_time("DEVICE-2")
