import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Enter the message: ").encode('ascii')
    client.sendto(msg, ('127.0.0.1', 55555))
    
    msg1, addr = client.recvfrom(1024)
    print(msg1.decode('ascii'))