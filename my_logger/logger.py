import sys
import smtplib
from email.mime.text import MIMEText

class LogLevel:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

class ConsoleHandler:
    def __init__(self, min_level):
        self.min_level = min_level

    def handle(self, level, message):
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

class FileHandler:
    def __init__(self, filename, min_level):
        self.filename = filename
        self.min_level = min_level

    def handle(self, level, message):
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
        
        with open(self.filename, "a") as f:
            print(f"[{prefix}] {message}", file=f)

class EmailHandler:
    def __init__(self, smtp_server, from_address, to_address, subject, min_level):
        self.smtp_server = smtp_server
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject
        self.min_level = min_level

    def handle(self, level, message):
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

        msg = MIMEText(f"[{prefix}] {message}")
        msg['From'] = self.from_address
        msg['To'] = self.to_address
        msg['Subject'] = self.subject

        smtp = smtplib.SMTP(self.smtp_server)
        smtp.send_message(msg)
        smtp.quit()

class ServerAPIHandler:
    def __init__(self, api_url, min_level):
        self.api_url = api_url
        self.min_level = min_level

    def handle(self, level, message):
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

        # code to send the log message to the server API goes here

class Logger:
    def __init__(self, min_level=LogLevel.DEBUG):
        self.min_level = min_level
        self.handlers = {}

    def add_console_handler(self, min_level=LogLevel.DEBUG):
        self.handlers['console'] = ConsoleHandler(min_level)

    def add_file_handler(self, filename, min_level=LogLevel.DEBUG):
        self.handlers['file'] = FileHandler(filename, min_level)

    def add_email_handler(self, smtp_server, from_address, to_address, subject, min_level=LogLevel.ERROR):
        self.handlers['email'] = EmailHandler(smtp_server, from_address, to_address, subject, min_level)

    def add_api_handler(self, api_url, min_level=LogLevel.ERROR):
        self.handlers['api'] = ServerAPIHandler(api_url, min_level)

    def debug(self, message, target='console'):
        self.log(LogLevel.DEBUG, message, target)

    def info(self, message, target='console'):
        self.log(LogLevel.INFO, message, target)

    def warning(self, message, target='console'):
        self.log(LogLevel.WARNING, message, target)

    def error(self, message, target='console'):
        self.log(LogLevel.ERROR, message, target)    
    
    def log(self, level, message, target):
        if level < self.min_level:
            return
        self.handlers[target].handle(level, message)

if __name__ == '__main__':
    logger = Logger(LogLevel.DEBUG)
    
    logger.add_console_handler(min_level=LogLevel.WARNING)

    logger.debug("This message won't be logged", target='console')
    logger.info("This message won't be logged", target='console')
    logger.warning("This is a warning message", target='console')
    logger.error("This is an error message", target='console')
