#!/usr/bin/env python

import json, socket
from threading import Thread

__author__ = "Wojciech Sadowski"
__credits__ = ["Wojciech Sadowski"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "wojtek2kdev@gmail.com"

class Server:

	Listener = {

	    'ENGINE' : []
			#other
	}

	Status = {

		"OK" : 200,
		"UNAUTHORIZED" : 401

	}

	TCP_IP = None
	TCP_PORT = None
	BUFFER_SIZE = None 
	SOCKET = None
	CONFIG = None

	def registerListener(self, listener, target):
		print 'CODE 002'
		{
			'engine' : Server.Listener['ENGINE']
		}[target].append(listener)
		print self.Listener['ENGINE']

	def getServerInfo(self):
		try:
			with open('config.json', 'r') as config:
				return json.loads(config.read())
		except Exception as e:
			print '[ERROR!]: ' + str(e)


	def __init__(self):
		
		self.CONFIG = self.getServerInfo()
		self.TCP_IP = self.CONFIG['ip']
		self.TCP_PORT = self.CONFIG['port']
		self.BUFFER_SIZE = self.CONFIG['buffer_size']  # Normally 1024, but we want fast response

		self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SOCKET.bind((self.TCP_IP, self.TCP_PORT))
		self.SOCKET.listen(1)

		listen = Thread(target=self.getDataFromClient, args=())
		listen.start()
	


	def sendDataToEngine(self, data):
		print 'CODE 001'
		print self.Listener['ENGINE'][0]
		for listener in self.Listener['ENGINE']:
			listener(data)


	def sendDataToListeners(self, target, data):
		try:
			{
				'engine' : self.sendDataToEngine
			}[target](data)
		except Exception as e:
			print e #'[WARN!]: Not found listener'

	def getDataFromClient(self):
		print __author__ + ' license: ' + __license__ + ' email: ' + __email__
		conn, addr = self.SOCKET.accept()
		print 'Connection address:', addr
		while 1:
		    data = conn.recv(self.BUFFER_SIZE)
		    try:
		    	if data:
			    	data = json.loads(data)
			    	self.sendDataToListeners(data['target'], data['code'])
		    except Exception as e:
		    	print '[ERROR!]: ' + str(e)
		    #if not data: break
		    print "received data:", data
		    conn.send(str(self.Status['OK']))  # echo
		conn.close()
'''
s = Server()
setServerInstance(s)'''