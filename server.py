from protocol import create_device, server_send, server_recv
import signal
import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 12345))
sock.listen(100)
conn = sock.accept()[0]
device = create_device()
active = True

while active:
    server_recv(conn, device)
    server_send(conn, device, 'pong')
