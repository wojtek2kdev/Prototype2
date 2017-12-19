from time import sleep
from server import Server
from pyA20.gpio import gpio, port

__author__ = "Wojciech Sadowski"
__credits__ = ["Wojciech Sadowski"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "wojtek2kdev@gmail.com"

class Engine:

	server = Server()
	move = 0

	Side = {

		"FRONT_LEFT" : port.PA12,
		"FRONT_RIGHT" : port.PA11

	}

	def __init__(self):
		gpio.init()
		server.registerListener(lambda move: setMove(move), 'ENGINE')
		for engine in [self.Side['FRONT_LEFT'], self.Side['FRONT_RIGHT']]:
			gpio.setcfg(engine, gpio.OUTPUT)

	def setMove(self, move):
		self.move = move

	def enableEngine(self, side):
		gpio.output(side, 1)

	def disableEngine(self, side):
		gpio.output(side, 0)

e = Engine()
e.disableEngine(e.Side['FRONT_LEFT'])



