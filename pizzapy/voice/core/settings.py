
from voice.enumerations import InputMode

ROOT_LOG_CONF = {
    'version': 1,
    'root': {
        'level': 'DEBUG',
        'handlers': ['file'],
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/log/jarvis.log',
            'mode': 'a',
            'maxBytes': 10000000,
            'backupCount': 3,
        },
    },
    'formatters': {
        'detailed': {
             'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    }
}


"""
Default General assistant settings
These values load in the MongoDB as the default values.
You can change the values when you start the assistant.
The application will ask you 'Do you want to configure it again (y/n)'
I you write yes you can change the following settings or you can change the following default values.
Keys Description:
    - assistant_name: Assistant name works as an activation word
    - enabled_period: A period (in seconds) that assistant is waked up (no need of other activation word)
    - input_mode: A mode could be 'InputMode.TEXT.value' or 'InputMode.VOICE.value'.
      In 'InputMode.TEXT.value' mode, the assistant waits to write in the console,
      and in 'InputMode.VOICE.value' to speak in configured mic.
    - response_in_text: If True: The assistant will print in the console the response
    - response_in_speech: If True: The assistant will produce voice response via audio output.               
"""


DEFAULT_GENERAL_SETTINGS = {
    'assistant_name': 'Jarvis',
    'enabled_period': 300,
    'input_mode': InputMode.TEXT.value,
    'response_in_speech': False,
}


"""
Google API Speech recognition settings
SpeechRecognition API : https://pypi.org/project/SpeechRecognition/2.1.3
Keys Description:
    - ambient_duration: Time for auto microphone calibration
    - pause_threshold: Minimum length silence (in seconds) at the end of a sentence
    - energy_threshold: Microphone sensitivity, for loud places, the energy level should be up to 4000
    - dynamic_energy_threshold: For unpredictable noise levels (Suggested to be TRUE)
"""
SPEECH_RECOGNITION = {
    'ambient_duration': 1,
    'pause_threshold': 1,
    'energy_threshold': 3000,
    'dynamic_energy_threshold': True
}


SKILL_ANALYZER = {
    'args': {
                "stop_words": None,
                "lowercase": True,
                "norm": 'l1',
                "use_idf": False,
            },
    'sensitivity': 0.2,

}


"""
Google text to speech API settings
"""
GOOGLE_SPEECH = {

    'lang': "en"
}


"""
Open weather map API settings
Create key: https://openweathermap.org/appid
"""
WEATHER_API = {
    'unit': 'celsius',
    'key': None
}


"""
WolframAlpha API settings
Create key: https://developer.wolframalpha.com/portal/myapps/
"""
WOLFRAMALPHA_API = {
    'key': None
}


"""
IPSTACK API settings
Create key: https://ipstack.com/signup/free
"""
IPSTACK_API = {
    'key': None
}
