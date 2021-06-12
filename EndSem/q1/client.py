import socket
import sys

# host and port number to connect to

HOST = '127.0.0.1'
PORT = 12000

p = int(input("Enter number to send :> "))

if __name__ == '__main__':
    # make a tcp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp connect client
    s.connect((HOST, PORT))
    s.send(bytes(str(p), 'utf-8'))  # send the data to the server in form of bytes
    sum_result = s.recv(
        1024
    ).decode()  # receive the result of the operation from the server
    print(f"The sum of the even digits : {sum_result}\n")
    # closing connection
    s.close()
