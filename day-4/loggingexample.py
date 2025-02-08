import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# DEBUG level: Detailed information, typically useful for diagnosing problems.
logging.debug("This is a debug message.")  

# INFO level: Informational messages that highlight the progress of the application.
logging.info("This is an info message.")  

# WARNING level: Indicates something unexpected happened, or a potential issue, but the program continues.
logging.warning("This is a warning message.")  

# ERROR level: Indicates a more serious problem that prevents the program from performing a function.
logging.error("This is an error message.")  

# CRITICAL level: Severe errors that may cause the program to terminate or a major failure.
logging.critical("This is a critical message.") 
