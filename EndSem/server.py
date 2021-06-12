import socket

#function to calculate sum of even digits
def findSum(n):
    s = 0
    while n > 0:
        r = n % 10
        if r % 2 == 0:
            s += r
        n = n // 10        
    return s

#declaring the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("server socket up and running....")

#declaring the port to be used for communication
port = 12345

#binding the socket to the  port 
sock.bind(('', port))
print("socket binded to ", port)

#port is listening for any requests
sock.listen(5)
print("sokcet is listening for connections")

#accepting the connection from
con, addr = sock.accept()
print("Got connection form ", addr)

#accepting the values calculating sum and then sending back to the user
while True:
    dt = con.recv(1024)
    if not dt:
        break
    num = int(dt.decode())
    print("The number received is ", str(num))
    ans = findSum(num)

    con.send(str(ans).encode())

#closing the connection
con.close()