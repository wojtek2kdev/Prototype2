#!/usr/bin/env python

import socket, json, time
from time import sleep

class Client:

	TCP_IP = '127.0.0.1'
	TCP_PORT = 1979
	BUFFER_SIZE = 1024
	SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __init__(self):
		self.TCP_IP = raw_input("ip (127.0.0.1 by default): ") or self.TCP_IP
		port = raw_input('port (1979 by default): ')
		self.TCP_PORT = int(port) if port else self.TCP_PORT

	def sendData(self, data):
		self.SOCKET.connect((self.TCP_IP, self.TCP_PORT))
		self.SOCKET.send(data)
		sleep(3)
		self.SOCKET.send(json.dumps({'target': 'engine', 'code': 1}))
		while 1:
			recv = self.SOCKET.recv(self.BUFFER_SIZE)
			time.sleep(0.5)
		#self.SOCKET.close()
		return recv

c = Client()
c.sendData(json.dumps({'target': 'engine', 'code': 0}))