from engine import Engine
from server import Server
import Queue
from threading import Thread
from time import sleep

queue = Queue.Queue()

e = Engine()
s = Server()

e.register(s)

'''
def startServer(q):
	s = Server()
	q.put(s)

def startEngine(q):
	s = q.get()
	print s
	e = Engine(s)
	while 1:
		print e.move
		sleep(1)

server = Thread(target=startServer, args=(queue,))
engine = Thread(target=startEngine, args=(queue,))
engine.start()
server.start()

queue.join()

print 'Done'

'''