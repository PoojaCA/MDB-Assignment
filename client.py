# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:23:30 2021

@author: User
"""

import socket
client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1',port))
#recieve connection message from server
msg = input("-> ")
while True:
    if msg == 'exit':
        break;
    else:
        client_socket.send(msg.encode())
    msg = input("-> ")
client_socket.close()