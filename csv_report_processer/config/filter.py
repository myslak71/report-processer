from logging import INFO


class LogLevelFilter:
    def __init__(self, level=INFO):
        self.__level = level

    def filter(self, log_record):
        return log_record.levelno == self.__level
