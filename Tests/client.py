#!/usr/bin/env python

import socket, json, time
from time import sleep
from pynput import keyboard
from threading import Thread

class Client:

	TCP_IP = '192.168.0.106' #'127.0.0.1'
	TCP_PORT = 1979
	BUFFER_SIZE = 1024
	SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	ENABLE = 0

	def __init__(self):
		self.TCP_IP = raw_input("ip (127.0.0.1 by default): ") or self.TCP_IP
		port = raw_input('port (1979 by default): ')
		self.TCP_PORT = int(port) if port else self.TCP_PORT
		t2 = Thread(target=self.detectKeys, args=())
		t2.start()
		t1 = Thread(target=self.sendData, args=())
		t1.start()
		

	def on_press(self, key):
	    try:
	        if key.char == 'w': self.ENABLE = 1
	    except AttributeError:
	        print('special key {0} pressed'.format(
	            key))

	def on_release(self, key):
	    self.ENABLE = 0
	    if key == keyboard.Key.esc:
	        # Stop listener
	        return False

	# Collect events until released
	def detectKeys(self):
		with keyboard.Listener(
	        on_press=self.on_press,
	        on_release=self.on_release) as listener:
	    		listener.join()

	def sendData(self):
		self.SOCKET.connect((self.TCP_IP, self.TCP_PORT))
		#self.SOCKET.send(data)
		self.SOCKET.send(json.dumps({'target': 'engine', 'code': 1}))
		while 1:
			recv = self.SOCKET.recv(self.BUFFER_SIZE)
			time.sleep(0.05)
			if self.ENABLE == 0: 
				#log.out('info', 'Send code to server', 'sendData', 'Engine')
				self.SOCKET.send(json.dumps({'target': 'engine', 'code': 0}))
			else:
				self.SOCKET.send(json.dumps({'target': 'engine', 'code': 1}))
		#self.SOCKET.close()
		return recv

c = Client()