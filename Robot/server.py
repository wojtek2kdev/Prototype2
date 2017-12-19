#!/usr/bin/env python

import json, socket

class Server:

	def getServerInfo():
		try:
			with open('config.json', 'r') as config:
				return json.loads(config.read())
		except Exception as e:
			print e

	CONFIG = getServerInfo()
	TCP_IP = CONFIG['ip']
	TCP_PORT = CONFIG['port']
	BUFFER_SIZE = CONFIG['buffer_size']  # Normally 1024, but we want fast response

	SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	SOCKET.bind((TCP_IP, TCP_PORT))
	SOCKET.listen(1)

	Listener = {

		'ENGINE' : []
		#other

	}

	Status = {

		"OK" : 200,
		"UNAUTHORIZED" : 401

	}

	def registerListener(self, listener, _type):
		{
			'engine' : Listener['ENGINE']
		}[_type].append(listener)

	def getDataFromClient(self):
		conn, addr = SOCKET.accept()
		print 'Connection address:', addr
		while 1:
		    data = conn.recv(BUFFER_SIZE)
		    #if not data: break
		    print "received data:", data
		    conn.send(self.Status['OK'])  # echo
		conn.close()
