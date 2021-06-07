from random import choice, randint

greetings = ['hey', 'hi', 'hello']
status = ['amazing', 'awesome', 'I am great today! How are you doing today?']
thank = ['you are welcome', 'all good']

def greeting(AI, command):
	AI.speak(choice(greetings))

# how are you
def hru(AI, command):
	AI.speak(choice(status))

def thanks(AI, command):
	AI.speak(choice(thank))

def repeat(AI, command):
	try:
		with open(AI.cachePath + 'last.txt', 'r') as file:
			last = file.readline()
			if last == 'failed':
				AI.speak('Your last command failed')
			elif last:
				exec(last)
			else:
				AI.speak('You have not said anything yet :(')
	except:
		AI.speak('You have not said anything yet')
