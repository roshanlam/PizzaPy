import logging
import sys
import time
from datetime import datetime

from voice.skills.assistant_skill import AssistantSkill
from voice.utils.console import clear
from voice.utils.startup import play_activation_sound
from voice.utils.mongoDB import db
from voice.enumerations import InputMode, MongoCollections

# FileName: Assistant Activation


class ActivationSkills(AssistantSkill):
    @classmethod
    def enable_assistant(cls, **kwargs):
        """
        Plays activation sound and creates the assistant response according to the day hour.
        """
        input_mode = db.get_documents(collection=MongoCollections.GENERAL_SETTINGS.value)[0]['input_mode']
        if input_mode == InputMode.VOICE.value:
            try:
                play_activation_sound()
            except Exception as e:
                logging.error("Error with the execution of skill with message {0}".format(e))
                cls.response("Sorry I faced an issue")
            time.sleep(1)
        cls.assistant_greeting(kwargs)

    @classmethod
    def disable_assistant(cls, **kwargs):
        """
        - Clear console
        - Shutdown the assistant service
        """
        cls.response('Bye')
        time.sleep(1)
        clear()
        logging.debug('Application terminated gracefully.')
        sys.exit()

    @classmethod
    def assistant_greeting(cls, *kwargs):
        """
        Assistant greeting based on day hour.
        """
        now = datetime.now()
        day_time = int(now.strftime('%H'))

        if day_time < 12:
            cls.response('Good morning')
        elif 12 <= day_time < 18:
            cls.response('Good afternoon')
        else:
            cls.response('Good evening')
