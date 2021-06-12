import socket

HOST = '127.0.0.1'  # localhost
PORT = 12000        # Port number to listen 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #checking the given cond 
        print('Connected from:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            even_sum = 0
            invalid = False
            data = str(data.decode())

            for ch in data:
                #iterating through each character in sent data
                try:
                    if int(ch) % 2 == 0:
                        even_sum += int(ch)
                except ValueError:
                    invalid = True
                    break
            even_sum = str(even_sum) #converting to string before sending and encdoing them 
            if invalid:
                conn.sendall(str("invalid Data").encode()) #this encode this backs to bytestream 
                print("Invalid Data Recieved")
            else:
                conn.sendall(even_sum.encode())
                print("Even Sum of Digits returned")
            