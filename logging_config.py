import logging
import os 

def setup_logging():
    """
    This configures the appaclitions logging 
    system. This is not meant to be ran directly
    """
    LOG_DIR = "logs"
    INFO_LOG_FILE = os.path.join(LOG_DIR, "info.log") 
    ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.log")
    CONSOLE_LOG_LEVEL = logging.DEBUG

    ## Making sure the log directory exsist
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        for handler in logger.handlers[:]: # Iterate over a copy of the list
            logger.removeHandler(handler)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')