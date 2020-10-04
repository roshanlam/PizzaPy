from sys import platform
from termcolor import colored 

if platform == 'win32':
	import colorama
	colorama.init()

def red(value):
	return colored(value, 'red', attrs=['bold'])

def green(value):
    return colored(value, 'green', attrs=['bold'])

def white(value):
    return colored(value, 'white', attrs=['bold'])

def yellow(value):
    return colored(value, 'yellow', attrs=['bold'])
