import socket 

client_socket= socket.socket()
host='127.0.0.1'
port = 11596 

print("Trying for Connection")
try:
    client_socket.connect((host,port))
except socket.error as e:
    print(str(e))

response = client_socket.recv(1024)
while True:
    data_input = input("Client Say Something > ")
    client_socket.send(str.encode(data_input))
    response = client_socket.recv(1024)
    print(f"From Server: {response.decode()}")

client_socket.close()

