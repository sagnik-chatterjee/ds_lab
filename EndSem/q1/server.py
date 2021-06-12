import socket
import sys

# host and port number to connect to
HOST = '127.0.0.1'
PORT = 12000

# func to calc the sum of even digits
def sumEvenDigits(n):
    s = 0
    while s > 0:
        r = n % 10
        if r % 2 == 0:
            s += r
        n = n // 10
    return s


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp connection
    s.bind((HOST, PORT))
    s.listen()  # listen for upcoming conenctions from the client
    print("Waiting for incoming connections...\n")
    while True:
        conn,addr=s.accept()
        # connection occured and print the location from where connection occured

        print(f"Received connections from {addr[0]} , (  {addr[1]} )\n")
        val = conn.recv(1024).decode()  # received the input and decode into the  value
        # from bytes
        print(f"{val} received from client")
        sum1 = sumEvenDigits(int(val))
        conn.send(bytes(str(sum1), 'utf-8'))  # send back the data as form of bytes
