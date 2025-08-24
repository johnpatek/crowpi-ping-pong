from protocol import create_device, server_send, server_recv
import signal
import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
device = create_device()
active = True


def sigcb(sig, frame):
    sock.close()
    active = False

while active:
    client_send(sock, device, 'ping)
    client_recv(sock, device)


