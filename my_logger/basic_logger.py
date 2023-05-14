import sys

class LogLevel:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

class BasicLogger:
    def __init__(self, min_level=LogLevel.DEBUG):
        self.min_level = min_level

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def warning(self, message):
        self.log(LogLevel.WARNING, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

    def log(self, level, message):
        if level < self.min_level:
            return
        
        if level == LogLevel.DEBUG:
            prefix = "DEBUG"
        elif level == LogLevel.INFO:
            prefix = "INFO"
        elif level == LogLevel.WARNING:
            prefix = "WARNING"
        elif level == LogLevel.ERROR:
            prefix = "ERROR"
        
        print(f"[{prefix}] {message}", file=sys.stderr)


logger = BasicLogger(LogLevel.DEBUG)

logger.debug("This message won't be logged")
logger.info("This message won't be logged")
logger.warning("This is a warning message")
logger.error("This is an error message")
