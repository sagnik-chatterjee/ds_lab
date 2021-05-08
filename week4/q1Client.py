"""
Author: Sagnik Chatterjee
UDP time server to display the current time and day
"""
import socket

host_udp="127.0.0.1"
port_udp=20001
bufferSize = 1024


msgFromClient = "Some random message from client side"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = (host_udp,port_udp)

# Create a UDP socket at client side
udpClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
udpClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = udpClientSocket.recvfrom(bufferSize)
print(f"Message from Server :=  {format(msgFromServer[0])}")

