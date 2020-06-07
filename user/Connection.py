# -*- coding: utf-8 -*-

import socket

class Connection(object):
    def __init__(self):
        self.MAX_BYTES = 1024
    
    def udp_socket_init(self):
        self.udp_socket_connected = False
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.sendto(''.encode(), ('', 1060)) # WORK AROUND, SORRY
        self.udp_port = self.udp_socket.getsockname()[1]
        self.udp_socket_settimeout()
    
    def udp_socket_settimeout(self, time = 0.01):
        self.udp_socket.settimeout(time)

    def udp_socket_connect(self, address):
        self.udp_socket.connect(address)
        self.udp_socket_connected = True
    
    def udp_socket_send_bytes(self, data = b''):
        if (self.udp_socket_connected):
            self.udp_socket.send(data)

    def udp_socket_recv_bytes(self):
        if (not self.udp_socket_connected):
            return None
        try:
            data = self.udp_socket.recv(self.MAX_BYTES)
        except socket.timeout:
            data = None
        return data