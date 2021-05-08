"""
AUTHOR: SAGNIK CHATTERJEE
Write a UDP simple chat program for message send and receive.

"""

import socket

# address is a tuple of the port and the host
address = ("127.0.0.1", 9000)
bufferSize = 1024

udpClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while True:
    print("Do Ctrl+c to exit the program !!")
    input_value = input("Type some text to send =>  ")
    print(f"1. Client Sent: {input_value} ")
    bytesToSend = str.encode(input_value)
    udpClientSocket.sendto(bytesToSend, address)
    msgFromServer = udpClientSocket.recvfrom(bufferSize)
    print(f"2. Client received: {msgFromServer}")
