import socket

# udp base conenctions
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname() #getting the host ip
udp_port = 9000  # this port should be connected

sock.bind((udp_host, udp_port))

while True:
    # stay connected until client found and received data
    print(f"Started the server at port := {udp_port}")
    data, addr = sock.recvfrom(1024)
    print(f"Received Messages:- {data.decode()} from {addr}")
