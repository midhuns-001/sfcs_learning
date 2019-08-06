import logging
import os
from logging.handlers import RotatingFileHandler
import json, sys

class JsonFormatter(logging.Formatter):
    """
        A custom formatter to format logging records as json strings.
    """

    def jsonify_log_record(self, log_record):
        """Returns a json string of the log record."""
        json_formated_output = None
        try:
            json_formated_output = json.dumps(log_record, indent=5, sort_keys=True)
        except:
            json_formated_output = log_record
        return json_formated_output   
    
    def format(self, record):
        """Formats a log record and serializes to json"""
        if isinstance(record.msg, dict):
            record.msg = self.jsonify_log_record(record.msg)
            
        result = super().format(record)
        return result


def initialize_logger(file_name, logs_dir=os.path.join(os.path.curdir, "logs")):
    """
        This method initializes the python log and set the formatting and debug level
        
    Parameters:
    file_name (str)
    logs_dir (str)
    Returns:
    returns a logger object
    
    """
#     Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    formatter = JsonFormatter(fmt='%(asctime)s:%(pathname)s:%(lineno)s:%(funcName)s:%(levelname)-5s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # If Directory not exist then create log directory
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    file_handler = RotatingFileHandler(os.path.join(logs_dir , "sfcs_execution.log"), maxBytes=(1048576 * 100), backupCount=7)
    file_handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(screen_handler)
    return logger

logger = initialize_logger(__name__)