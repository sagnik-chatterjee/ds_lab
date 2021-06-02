from functools import reduce
from dateutil import parser
import threading
import datetime
import socket
import time

client_data = {}

"""
nesting thread function used to receive clock time from a conencted client 
"""


def start_receive_clock_tim(connector, address):
    while True:
        clock_time_string = connector.recv(1024).decode()
        clock_time = parser.parse(clock_time_string)
        clock_time_diff = datetime.datetime.now() - clock_time

        client_data[address] = {
            "clock_time": clock_time,
            "time_difference": clock_time_diff,
            "connector": connector,
        }

        print(f"Client data updated with {address} ")
        time.sleep(5)


"""
master thread function used to open portal for accepting clients over given port 
"""


def start_connecting(master_servant):
    while True:
        master_slave_connector, addr = master_servant.accept()
        slave_address = str(addr[0]) + " : " + str(addr[1])
        print(f"{slave_address} got successfully connected.")

        current_thread = threading.Thread(
            target=start_receive_clock_tim,
            args=(
                master_slave_connector,
                slave_address,
            ),
        )
        current_thread.start()


def get_avg_clock_diff():
    current_client_data = client_data.copy()
    time_difference_list = list(
        client["time difference"] for client_addr, client in client_data.items()
    )

    sum_of_clk_diff = sum(time_difference_list, datetime.timedelta(0, 0))

    avg_clock_diff = sum_of_clk_diff / len(client_data)

    return avg_clock_diff


def sync_all_clocks():
    while True:
        print("New sync cycle started")
        print(f"Number of clients to be synced : {len(client_data)}")
        if len(client_data) > 0:
            avg_clock_diff = get_avg_clock_diff()
            for client_addr, client in client_data.items():
                try:
                    sync_time = datetime.datetime.now() + avg_clock_diff

                    client["connector"].send(str(sync_time).encode())

                except Exception as e:
                    print(
                        f"Some problem occured while sending sync time through {client_addr}"
                    )

        else:
            print(f"No client data , sync not applicable")
            time.sleep(5)


def intiate_clock_server(port=8080):
    master_server = socket.socket()
    master_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket at master node created successfully")
    master_server.bind(("", port))
    master_server.listen(10)
    print("Clock server started ...\n")
    print("Starting to make connections ....\n")

    master_thread = threading.Thread(target=start_connecting, args=(master_server,))
    master_thread.start()

    print("Starting sync parallely...\n")
    sync_thread = threading.Thread(target=sync_all_clocks, args=())
    sync_thread.start()


if __name__ == "__main__":
    intiate_clock_server(port=8080)
