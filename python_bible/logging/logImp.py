import logging

# logging.info("First informational message!")
# logging.critical("This is serious!")

#####################################################################
#                   CREATING LOGGERS                                #
# using the  constructor of the Logger class or by using the method #
# getLogger
# 1. DEBUG
# 2. INFO
# 3. WARNING
# 4. ERROR
# 5. CRITICAL                                                        #
######################################################################

# logger = logging.getLogger()
logger = logging.Logger("MyLOGGER")

# We can either directly call the function of the respective security level
logger.info("Logger successfully created!")
logger.critical("Critical Message!")

# we can use the method log and specify the security level in the parameters
logger.log(logging.INFO, "Successful!")
logger.log(logging.CRITICAL, "Critical!")

# we need to adjust the level of the logger and second of all, we need to remove all of the
# handlers from the default root logger.

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)
