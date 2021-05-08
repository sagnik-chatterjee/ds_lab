"""
Author: Sagnik Chatterjee
UDP time server to display the current time and day
"""
import socket
import time

host_udp = "127.0.0.1"
port_udp  = 20001
bufferSize = 1024

currT = time.ctime(time.time())
bytesToSend = str.encode(currT)

# Create a datagram socket
udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
udpServerSocket.bind((host_udp, port_udp))

print(f"Started UDP server at port = {port_udp} ...")
# Listen for incoming datagrams
while True:
    bytesAddressPair = udpServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print(f"Message from Client:= {message}")
    print(f"Client IP Address:= {address}")
    # Sending a reply to client
    udpServerSocket.sendto(bytesToSend, address)
