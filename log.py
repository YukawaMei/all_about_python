import logging
import os
from logging import StreamHandler
from typing import Final

from concurrent_log_handler import ConcurrentRotatingFileHandler
from flask.logging import default_handler

from utils import DirectoryHelper

BASE_DIR = DirectoryHelper.root_path()
LOG_PATH = os.path.join(BASE_DIR, 'log')

# log file max size 100MB
LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
# log file rotation number 10
LOG_FILE_BACKUP_COUNT = 10

formatter = logging.Formatter('%(process)d-%(threadName)s-%(levelname)s:%(asctime)s'
                              '[%(filename)s:line:%(lineno)d]:"%(message)s" from function: %(funcName)s')


class Logger:
    # used to save the class attributes of the object
    instance = None
    logger_map = {}

    def __new__(cls):
        if cls.instance is None:
            obj = super(Logger, cls).__new__(cls)
            cls.instance = obj
        return cls.instance

    def __init__(self):
        pass

    @staticmethod
    def app_logger(app, level=logging.DEBUG):
        # remove default handler
        app.logger.removeHandler(default_handler)
        app.logger.propagate = False

        # save log to files
        # 1 MB = 1024 * 1024 bytes
        # set the log file size to 100MB, after exceeding 100MB,
        # automatically start writing new log files, history file archived
        file_handler_info = ConcurrentRotatingFileHandler(
            filename=os.path.join(LOG_PATH, 'all_about_python.log'),
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(level)
        app.logger.addHandler(file_handler_info)

        file_handler_error = ConcurrentRotatingFileHandler(
            filename=os.path.join(LOG_PATH, 'all_about_python_error.log'),
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)

        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level)

        app.logger.addHandler(stream_handler)
        app.logger.setLevel(level)

    @staticmethod
    def get_logger(name='', level=logging.DEBUG):
        logger = logging.getLogger(name)
        logger.propagate = False
        file_handler_info = ConcurrentRotatingFileHandler(
            filename=os.path.join(LOG_PATH, name + '.log'),
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(level)
        logger.addHandler(file_handler_info)

        file_handler_error = ConcurrentRotatingFileHandler(
            filename=os.path.join(LOG_PATH, name + '_error.log'),
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        logger.addHandler(file_handler_error)

        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level)
        logger.addHandler(stream_handler)

        logger.setLevel(level)
        Logger.logger = logger
        return logger

    @staticmethod
    def build(name='all_about_python', level=logging.DEBUG):
        if not Logger.logger_map.__contains__(name):
            Logger.logger_map[name] = Logger.get_logger(name, level)
        return Logger.logger_map[name]


logger: Final = Logger.build(level=logging.INFO)
