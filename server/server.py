#Temporary file
import socket

MAX_BYTES = 1500

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listing at', sock.getsockname())

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        sock.sendto(data, address)
    
server("", 1060)
