import logging
from voice.skills.assistant_skill import AssistantSkill
from voice.utils.mongoDB import db
from voice.utils.console import add_dashes


class AssistantInfoSkills(AssistantSkill):
    @classmethod
    def assistant_check(cls, **kwargs):
        """
        Responses that assistant can hear the user.
        """
        cls.response('Yes, I hear you!')

    @classmethod
    def tell_the_skills(cls, **kwargs):
        """
        Tells what he can do as assistant.
        """
        try:
            response_base = 'I can do the following: \n\n'
            response = cls._create_skill_response(response_base)
            cls.response(response)
        except Exception as e:
            logging.error("Error with the execution of skill with message {0}".format(e))
            cls.response("Sorry I faced an issue")

    @classmethod
    def assistant_help(cls, **kwargs):
        """
        Assistant help prints valuable information about the application.
        """
        cls.console(add_dashes('Help'))
        response_base = ''
        try:
            response = cls._create_skill_response(response_base)
            cls.console(response)
        except Exception as e:
            logging.error("Error with the execution of skill with message {0}".format(e))
            cls.response("Sorry I faced an issue")

    @classmethod
    def _create_skill_response(cls, response):

        #################################################
        ######## For existing skills (basic skills) #####
        #################################################
        
        basic_skills = db.get_documents(collection='enabled_basic_skills')
        response = response + '* Basic Enabled Skills:' + '\n'
        for skill_id, skill in enumerate(basic_skills, start=1):
            response = response + '{0}) '.format(skill_id) + skill.get('description') + '\n'

        #######################################################
        ## For learned skills (created from 'learn' skill) ####
        #######################################################
        skills = db.get_documents(collection='learned_skills')
        response = response + '\n' + '* Learned Skills:' + '\n'
        for skill_id, skill in enumerate(skills, start=1):
            message = 'Learned skill - Q: ' + skill.get('tags') + ' | R: ' + skill.get('response')
            response = response + '{0}) '.format(skill_id) + message + '\n'

        return response
