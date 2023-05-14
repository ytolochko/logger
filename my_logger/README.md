# Logger
The Logger library provides a simple way to log messages to different targets, such as the console, a file, email, or a server API.

Usage
To use the Logger library, you first need to create a Logger instance, then add a handler and finally call a logging method with a specified target, e.g.: 

```from logger import Logger, LogLevel
logger = Logger()
logger.add_console_handler(min_level=LogLevel.DEBUG)
logger.debug("This message is a debug message", target='console')
```

This creates a logger, and adds a console handler that accepts all log levels. You can change the minimum accepted log level by passing a different level to the constructor.

Here are the available choices of log levels:
```
DEBUG
INFO
WARNING
ERROR
```

Here are the available choices of log targets: 

Console Handler
The ConsoleHandler sends logs to the console. You can add it to the logger like this:

`logger.add_console_handler(LogLevel.WARNING)`
This will send all logs of severity WARNING and above to the console.

File Handler
The FileHandler sends logs to a file. You can add it to the logger like this:

`logger.add_file_handler("logfile.txt", LogLevel.DEBUG)`
This will send all logs of severity DEBUG and above to the file "logfile.txt".

Email Handler
The EmailHandler sends logs to an email address. You can add it to the logger like this:

`logger.add_email_handler("smtp.gmail.com", "me@gmail.com", "you@gmail.com", "Logger error", LogLevel.ERROR)`

This will send all logs of severity ERROR and above to the email address "you@gmail.com", using the SMTP server "smtp.gmail.com" and the subject line "Logger error".

Server API Handler (actual API logging functionality is currently not implemented)
The ServerAPIHandler sends logs to a server API. You can add it to the logger like this:

`logger.add_server_api_handler("https://api.example.com/logs", LogLevel.INFO)`
This will send all logs of severity INFO and above to the server API at "https://api.example.com/logs".

To log a message, simply call the appropriate method on the logger, e.g.:

```
logger.debug("Debug message", target='console')
logger.info("Info message", target='file')
logger.warning("Warning message", target='email')
logger.error("Error message", target='api)
```
You can also add different log handlers to the logger to send logs to different targets. Here are some examples:


You can add multiple handlers of different types to the same logger, and each log message will be sent to all the handlers that accept its severity level.

## Extra points 
1. Consider how and where we could make this Logger more open to modification.

One way to make the Logger more open to modification would be to allow users to define their own log handlers. Currently, the library provides four types of handlers: ConsoleHandler, FileHandler, EmailHandler, and ServerAPIHandler. These are the main use cases, there may be situations where users want to log messages to other targets, such as a database or a messaging system or something very user-specific.

Another idea of making this logger more open to modification, is to allow users to define their own message format by passing a format string to the logger constructor, as currently it is simply a log level + the actual message.


2. Give us your own ideas on how to improve this.

To make the Logger more open to modification, we could define an abstract base class for log handlers, and allow users to define their own custom handlers by subclassing this base class. This provide a flexible way for users to add their own log target handlers without interfering with already existing functionality. 

As to the second point, about defining a custom message format, implementing it would involve adding functionality to the `handle` method in the respective loggers to accept specific formatting options

3. Any improvements to the code that could simplify our Big O notation of every method? Any ways to remove loops, if, switches, etc?

In general, the functionality of the logger looks pretty efficient. In terms of Big O notation, its complexity is O(1), since the process of logging is an atomic operation and its runtime is not dependent on the size of the input. As such, 