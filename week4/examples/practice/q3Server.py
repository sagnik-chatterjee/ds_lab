import socket

HOST = '127.0.0.1' 
PORT = 31621

s = socket.socket()
s.bind((HOST, PORT))
s.listen()

print("  Waiting for incoming connections...\n")
conn, addr = s.accept()

print(f"Received connection from {addr[0]} ,{addr[1]} ",end="\n")
s_name = conn.recv(1024)
s_name = s_name.decode()

print(f"{s_name} has connected to the chat room \n Enter F to exit chat room\n")
name = input(str("Enter your name: "))
conn.send(name.encode())
while True:
    message = input(str("Me : "))
    if message == "F":
        message = "Left chat room! "
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"{s_name} : {message}")