import errno
import logging
import os
from logging.handlers import RotatingFileHandler

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def info(message):
    # method for info log
    logger = logging.getLogger('Misters-INFO')
    logger.setLevel(logging.INFO)
    filename = 'logs/Info/info.log'
    log_file_exists(filename)
    handler = RotatingFileHandler(filename, maxBytes=2000, backupCount=100)
    console = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(message)


def debug(message):
    # method for debug log
    logger = logging.getLogger('Misters-DEBUG')
    logger.setLevel(logging.DEBUG)
    filename = 'logs/Debug/debug.log'
    log_file_exists(filename)
    handler = RotatingFileHandler(filename, maxBytes=2000, backupCount=100)
    console = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(message)


def warning(message):
    # method for warning log
    logger = logging.getLogger('Misters-WARNING')
    logger.setLevel(logging.WARNING)
    filename = 'logs/Warning/warning.log'
    log_file_exists(filename)
    handler = RotatingFileHandler(filename, maxBytes=2000, backupCount=100)
    console = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.warning(message)


def error(message):
    # method for error log
    logger = logging.getLogger('Misters-ERROR')
    logger.setLevel(logging.ERROR)
    filename = 'logs/Error/error.log'
    log_file_exists(filename)
    handler = RotatingFileHandler(filename, maxBytes=2000, backupCount=100)
    console = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.error(message)


def log_file_exists(filepath):
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
            return True
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                return False
