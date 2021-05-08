'''
AUTHOR: SAGNIK CHATTERJEE
Write a program where client can send a message to the server and the server can receive
the message and send, or echo, it back to the client.
'''

import socket 

HOST="127.0.0.1"
PORT=9000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept() 

    with conn:
        print(f'Connected by  {addr}')
        while True:
            data = conn.recv(3000)
            if data:
                print(f"Client  {data.decode()}")
                data = input(f" > ")
                if not data:
                    break 
                #send back message as bytes to cleint 
                conn.sendall(bytearray(data,'utf-8'))
    conn.close()