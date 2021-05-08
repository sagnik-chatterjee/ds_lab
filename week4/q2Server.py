"""
AUTHOR: SAGNIK CHATTERJEE
Write a UDP simple chat program for message send and receive.

"""

import socket

host_udp = "127.0.0.1"
port_udp = 9000
bufferSize = 1024

udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpServerSocket.bind((host_udp,port_udp))

print(f"Started UDP server at port = {port_udp} ...")
# Listen for incoming datagrams
while True:
    print("Do Ctrl+c to exit the program !!")
    print("####### Server is listening #######")
    bytesAddressPair = udpServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print(f"2. Server Received : {message}")
    input_value = input("1.Type some text to send => ")
    bytesToSend = str.encode(input_value)
    udpServerSocket.sendto(bytesToSend, address)
    print(f"1. Server sent: {input_value}")
    print("####### Server is listening #######")
