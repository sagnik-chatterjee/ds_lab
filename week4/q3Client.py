"""
AUTHOR: SAGNIK CHATTERJEE

Write a TCP/UDP peer to peer chat system between two different machines.

"""
import sys
import socket
import threading


def connect(s):
    while True:
        r_msg = s.recv(1024)
        if not r_msg:
            break
        if r_msg == "":
            pass
        else:
            print(r_msg.decode())


def receive(s):
    while True:
        s_msg = input().replace("b", "").encode("utf-8")
        if s_msg == "":
            pass
        if s_msg.decode() == "exit":
            print("Exit")
            break
        else:
            s.sendall(s_msg)


if __name__ == "__main__":

    host = "127.0.0.1"
    port = 10000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port))
    print("Client Started")
    threada = threading.Thread(target=connect, args=([s]))
    threadb = threading.Thread(target=receive, args=([s]))
    threada.start()
    threadb.start()
    threada.join()
    threadb.join()
