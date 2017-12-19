#!/usr/bin/env python

import json

def getServerInfo():
	try:
		with open('config.json', 'r') as config:
			return json.loads(config.read())
	except Exception as e:
		print e


import socket


config = getServerInfo()

TCP_IP = config['ip']
TCP_PORT = config['port']
BUFFER_SIZE = config['buffer_size']  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()
