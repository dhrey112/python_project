import logging

logger = logging.getLogger("MyLOGGER")  # defining a logger
logger.setLevel(logging.INFO)  # set the security level

handler = logging.FileHandler("logfile.log")  # FileHandler that logs into the file logfile.log
handler.setLevel(logging.INFO)  # set the security level  again

logger.addHandler(handler)  # add the handler to our logger using the addHandler function
logger.info("Log this into the file!")
logger.critical("This is critical!")


