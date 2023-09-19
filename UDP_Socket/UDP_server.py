import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = '127.0.0.1'
PORT = 55555

server.bind((HOST, PORT))

while True:
    msg, addr = server.recvfrom(1024)
    print('Server Executed!!')
    server.sendto(msg, addr)