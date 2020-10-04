import os 
import sys 
import json 
import importlib
import shutil
import pyttsx3
import speech_recognition as sr 

from voice.core.scripts.colors import red, yellow, green, white

class AI:
	def __init__(self, abilitiesPath = 'Data/Abilities/', cachePath = 'Data/Cache/', integrate = True):
		self.abilitiesPath = abilitiesPath
		self.cachePath = cachePath

		self.recogninzer = sr.Recogninzer()
		self.microphone = sr.Microphone()

		# wake up words for the AI
		self.wake = ['Jarvis', 'Roshan', 'AI']

		self.responses = { 'yes': ['yes', 'yep', 'yeah', 'ya'],
						   'no' : ['no', 'nah', 'nope']
						  }

		try:
			self.engine = pyttsx3.init()
		except ModuleNotFoundError:
			print(red('\n[-] Dependency Not Found!'))
			print(yellow('[!] Install \"pywin32\" to Continue...'))
			sys.exit(0)

