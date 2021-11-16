import logging
from logging import handlers
import logging.config

# use config file to set config
#logging.config.dictConfig('logging.conf')
#logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample') # logger defined in helper.py
print(logger.name)
logger.debug('this is a debug message')

#change the log level from default, view docs for more info
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
datefmt='%m/%d/%Y %H:%M:%S')

# 5 different log levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# using helper module, good practice to import logger in this way
# create hierarchy of loggers
import helper


try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    #log the stack trace
    logging.error(e, exc_info=True)


import traceback


try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    #log the stack trace
    logging.error("The error is %s", traceback.format_exc())


from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#after 2k bytes it will roll over the log another  & keep backups app.log1, app.log2, app.log3, etc
handler =RotatingFileHandler('app.log', maxBytes=2000,backupCount=5)
logger.addHandler(handler)

##All of this is sent to the log file
for _ in range(100000):
    logger.info('Hello world!')


#Timed rotating file handler
from logging.handlers import TimedRotatingFileHandler
import time
#creates rotating lock based on how much time has passed

# s, m, h, d, midnight, w0 = monday, w1 = tuesday, etc
hanlder = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)
for _ in range(6):
    logger.info('Hello world!')
    time.sleep(5)


