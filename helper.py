import logging
# create logger called helper
logger = logging.getLogger(__name__)
logger.propagate = False # prevnts propogation of hierarchy to base logger
logger.info('hello from helper')

logger = logging.getLogger('simpleExample')

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')


# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')



