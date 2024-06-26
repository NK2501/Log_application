# Log_application
#Logger Module

#Overview
 
 This logger module is designed to provide a robust and configurable logging solution for any Python codebase. It supports log rotation and custom log formatting, 
 ensuring that log messages are stored efficiently and in a structured format.

#Features

 Log messages are saved to a file at a configurable location.
 Logs include the following information:
 1) Timestamp
 2) Log Level (DEBUG, INFO, ERROR)
 3) File name (source code file from which the log was created)
 4) Function name (function name from which log creation was invoked)
 5) Thread ID
 6) Actual log message
 7) Log file rotation is handled after every 5 MB, with a limit of 10 rotations. Old logs are automatically wrapped around.

#Installation

 To use this logger module, you can simply include the logger_module.py file in your project.

#Usage

 To use this logger in any part of your codebase, simply import the get_logger function and use the returned logger instance to log messages.
 1) Import the Logger:
    
    from logger_module import get_logger

 3) Get the Logger Instance:
    
    log = get_logger()

 5) Log Messages:
    
    def some_function():
       log.info("This is an info log message.")
       log.debug("This is a debug log message.")
       log.error("This is an error log message.")

#Logger Class

#Initialization:

    1) Sets up the logger with a RotatingFileHandler that handles log rotation after the log file reaches 5 MB.
   
    2) Configures the logger to keep up to 10 backup files.
   
    3) Defines a custom formatter to include the required fields in the log messages.

#Singleton Pattern

   Ensures only one instance of the logger is created and used throughout the application, preventing multiple handlers from writing to the same file.

#Log Format

 1.%(asctime)s: Timestamp of the log entry.
 
 2.%(levelname)s: Log level (DEBUG, INFO, ERROR).
 
 3.%(filename)s: Source code file name.
 
 4.%(funcName)s: Function name.
 
 5.%(thread)d: Thread ID.
 
 6.%(message)s: The actual log message.
 
#Conclusion

  This logger module provides a comprehensive logging solution that can be seamlessly integrated into any Python codebase. It ensures logs are stored in a well- 
  defined format and rotated efficiently, helping maintain clean and manageable log files.
