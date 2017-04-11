#!/usr/bin/env python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 9550))
sock.listen(5)

while True:
    client, ip = sock.accept()
    info = client.recv(10240)
    print info

while True:
    pass
