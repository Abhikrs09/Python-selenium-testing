from loguru import logger
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure the Logs directory exists
        log_dir = "./Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logger
        logger.add(os.path.join(log_dir, "automation.log"),
                   format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
                   level="INFO",
                   rotation="1 MB",  # Automatically rotate log file after reaching 1 MB
                   retention="7 days")  # Keep logs for 7 days

        return logger

# Example usage:
# logger = LogGen.loggen()
# logger.info("This is an info message.")
# logger.error("This is an error message.")
