import logging
import logging.handlers
import os

class Logger:
    def __init__(self, log_file_path=r'E:\DBDA\Log_application\log\app.log'):
        self.logger = logging.getLogger('CustomLogger')
        self.logger.setLevel(logging.DEBUG)

        # Ensure log directory exists
        log_dir = os.path.dirname(log_file_path)
        os.makedirs(log_dir, exist_ok=True)

        # Create a rotating file handler
        handler = logging.handlers.RotatingFileHandler(
            log_file_path, maxBytes=5 * 1024 * 1024, backupCount=10
        )
        
        # Custom log format
        formatter = logging.Formatter(
            fmt='%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(thread)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

# Singleton logger instance
_logger_instance = None

def get_logger():
    global _logger_instance
    if (_logger_instance is None):
        _logger_instance = Logger().get_logger()
    return _logger_instance

# Example usage
if __name__ == "__main__":
    log = get_logger()
    
    def example_function():
        log.info("This is an info log message.")
        log.debug("This is a debug log message.")
        log.error("This is an error log message.")

    example_function()
