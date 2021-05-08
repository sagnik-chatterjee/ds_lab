import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()  # getting the host ip

udp_port = 9000  # this port should be connected

msg = "This is some random message sent from client to server "
print(f"UDP target IP : {udp_host}")
print(f"UDP targte Port: {udp_port}")

sock.sendto(msg.encode(), (udp_host, udp_port))
