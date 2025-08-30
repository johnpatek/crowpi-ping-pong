import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message, textsize
from luma.core.sprite_system import framerate_regulator
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import socket

def create_device():
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
    return device

def print_message(device, msg, reverse=False):
    y_offset=0
    fill="white" 
    font=proportional(CP437_FONT)
    scroll_delay=0.1
    fps = 0 if scroll_delay == 0 else 1.0 / scroll_delay
    regulator = framerate_regulator(fps)
    font = font or DEFAULT_FONT
    with canvas(device) as draw:
        w, h = textsize(msg, font)

    x = device.width
    virtual = viewport(device, width=w + x + x, height=device.height)

    with canvas(virtual) as draw:
        text(draw, (x, y_offset), msg, font=font, fill=fill)

    if reverse:
        i = w + x
        while i >= 0:
            with regulator:
                virtual.set_position((i, 0))
                i -= 1
    else:
        i = 0
        while i <= w + x:
            with regulator:
                virtual.set_position((i, 0))
                i += 1

def client_send(sock, device, msg):
   print_message(device, msg, reverse=False)
   sock.send(msg.encode())

def client_recv(sock, device):
   msg = sock.recv(1024).decode()
   print_message(device, msg, reverse=True)

def server_send(sock, device, msg):
   print_message(device, msg, reverse=True)
   sock.send(msg.encode())

def server_recv(sock, device):
   msg = sock.recv(1024).decode()
   print_message(device, msg, reverse=False)
