"""
AUTHOR: SAGNIK CHATTERJEE

Write a TCP/UDP peer to peer chat system between two different machines.

"""

import sys
import socket
import threading


def connect(conn):
    while True:
        received = conn.recv(1024)
        if received == " ":
            pass
        else:
            print(received.decode())


def sendMsg(conn):
    while True:
        send_msg = input().replace("b", "").encode()
        if send_msg == " ":
            pass
        else:
            conn.sendall(send_msg)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 10000))
    s.listen()
    (conn, addr) = s.accept()
    print("Server Started...")
    threada = threading.Thread(target=connect, args=([conn]))
    threadb = threading.Thread(target=sendMsg, args=([conn]))
    threada.start()
    threadb.start()
    threada.join()
    threadb.join()
