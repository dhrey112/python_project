import logging

logger = logging.Logger("MYLOGGER")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logfile_formatted.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.info("This will get into the file!")