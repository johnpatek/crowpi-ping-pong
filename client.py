from protocol import create_device, client_send, client_recv
import signal
import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 12345))
device = create_device()
active = True

while active:
    client_send(sock, device, 'ping')
    client_recv(sock, device)
