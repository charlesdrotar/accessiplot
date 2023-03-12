import datetime
import logging
import os

__version__ = "0.0.1"

ct = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
LOGFILE_NAME = f'{ct}.log'
LOGGER_NAME = "accessiplot_logger"
LOGGING_DIRECTORY = ".accessiplot_logs"
LOGGING_PATH = os.path.join(LOGGING_DIRECTORY, LOGFILE_NAME)

# Attempt to make the logging directory
try:
    os.mkdir(LOGGING_DIRECTORY)
except FileExistsError:
    pass

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(LOGGING_PATH)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to LOGGER
logger.addHandler(ch)
logger.addHandler(fh)
print(f"Creating logger file at {LOGGING_PATH}")
