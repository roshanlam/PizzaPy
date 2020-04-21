
import logging
import time
from logging import config

from voice.core.processor import Processor
from voice import settings
from voice.settings import ROOT_LOG_CONF
from voice.utils.mongoDB import db
from voice.utils.startup import internet_connectivity_check, configure_MongoDB
from voice.core.console_manager import ConsoleManager

# Create a Console & Rotating file logger
config.dictConfig(ROOT_LOG_CONF)


def main():
    """
    Do initial checks, clear the console and print the assistant logo.
    STEP 1: Clear log file in each assistant fresh start
    STEP 2: Checks for internet connectivity
    STEP 3: Configuare MongoDB, load skills and settings
    STEP 4: Clear console
    """

    # STEP 1
    with open(ROOT_LOG_CONF['handlers']['file']['filename'], 'r+') as f:
        f.truncate(0)

    logging.info('Startup checks..')

    # STEP 2
    if not internet_connectivity_check():
        logging.warning('Skills with internet connection will not work :-(')
        time.sleep(3)

    # STEP 3
    configure_MongoDB(db, settings)

    # STEP 4
    console_manager = ConsoleManager()
    logging.info('Application started')
    console_manager.console_output()

    processor = Processor(settings, db)

    while True:
        processor.run()


if __name__ == '__main__':
    main()
