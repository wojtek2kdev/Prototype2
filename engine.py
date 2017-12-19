from time import sleep
from pyA20 import gpio, port

__author__ = "Wojciech Sadowski"
__credits__ = ["Wojciech Sadowski"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "wojtek2kdev@gmail.com"

Engine = {

	FRONT_LEFT : port.PA12,
	FRONT_RIGHT : port.PA11

}

gpio.init()
for engine in [Engine.FRONT_LEFT, Engine.FRONT_RIGHT]:
	gpio.setcfg(engine, gpio.OUTPUT)
gpio.output(Engine.FRONT_LEFT, 1)
