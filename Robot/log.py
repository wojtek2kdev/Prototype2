from datetime import datetime

INFO = '[INFO]: '
ERROR = '[ERROR!]: '
WARN = '[WARN!]: '

def out(_type, messages, function, base_class):
	print '[' + str(datetime.now().time())[:8] + ': FUNCTION: ' + function + ' at class: ' + base_class + ']'
	prefix = {
		'info' : INFO,
		'err' : ERROR,
		'warn' : WARN
	}[_type]
	for message in messages:
		print ' -> ' + prefix + message