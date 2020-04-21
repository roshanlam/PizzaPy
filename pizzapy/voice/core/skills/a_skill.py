import logging
import speech_recognition as sr

from voice.core.console_manager import ConsoleManager
from voice.utils.mongoDB import db
from voice.settings import SPEECH_RECOGNITION
from voice.enumerations import InputMode
import voice.engines as engines


class AssistantSkill:
    """
    This class is the parent of all skill classes.
    """
    first_activation = True
    console_manager = ConsoleManager()
    engine = None

    @classmethod
    def console(cls, text):
        cls.console_manager.console_output(text)

    @classmethod
    def response(cls, text):
        cls.set_engine()
        cls.engine.assistant_response(text)

    @classmethod
    def extract_tags(cls, voice_transcript, tags):
        """
        This method identifies the tags from the user transcript for a specific skill.
        e.x
        Let's that the user says "hi jarvis!".
        The skill analyzer will match it with enable_assistant skill which has tags 'hi, hello ..'
        This method will identify the that the enabled word was the 'hi' not the hello.
        :param voice_transcript: string
        :param tags: string
        :return: set
        """
        try:
            transcript_words = voice_transcript.split()
            tags = tags.split(',')
            return set(transcript_words).intersection(tags)
        except Exception as e:
            logging.error("Failed to extract tags with message {0}".format(e))
            return set()

    @classmethod
    def set_engine(cls):
        if not cls.engine and not db.is_collection_empty(collection='general_settings'):
            cls.engine = engines.TTSEngine() if db.get_documents(collection='general_settings')[0]['response_in_speech']\
                    else engines.TTTEngine()
