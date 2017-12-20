from time import sleep
import log
#from pyA20.gpio import gpio, port

__author__ = "Wojciech Sadowski"
__credits__ = ["Wojciech Sadowski"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "wojtek2kdev@gmail.com"

class Engine:

	move = 0

	'''Side = {

		"FRONT_LEFT" : port.PA12,
		"FRONT_RIGHT" : port.PA11

	}'''

	def __init__(self):
		#gpio.init()
		log.out('info', ['Engine module enabled!', 'Init pinout..'], '__init__', 'Engine')
		#for engine in [self.Side['FRONT_LEFT'], self.Side['FRONT_RIGHT']]:
			#gpio.setcfg(engine, gpio.OUTPUT)

	def register(self, Server):
		Server.registerListener(lambda move: self.setMove(move), 'engine')

	def setMove(self, move):
		self.move = move
		log.out('info', ['Move code: ' + move], 'setMove', 'Engine')

	def enableEngine(self, side):
		gpio.output(side, 1)

	def disableEngine(self, side):
		gpio.output(side, 0)

#e.disableEngine(e.Side['FRONT_LEFT'])



