from time import sleep
from pyA20.gpio import gpio, port

__author__ = "Wojciech Sadowski"
__credits__ = ["Wojciech Sadowski"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "wojtek2kdev@gmail.com"

class Engine:

	Side = {

		"FRONT_LEFT" : port.PA12,
		"FRONT_RIGHT" : port.PA11

	}

	def __init__(self):
		gpio.init()
		for engine in [Side['FRONT_LEFT'], Side['FRONT_RIGHT']]:
			gpio.setcfg(engine, gpio.OUTPUT)

	def enableEngine(self, side):
		gpio.output(side, 1)

	def disableEngine(self, side):
		gpio.output(side, 0)

e = Engine()
e.disableEngine(e.Side['FRONT_LEFT'])



