# Built-in Module in Python
import logging

# Create a custom format
fmt = '%(asctime)s : User, %(user)-8s , has issue: %(message)s'

logging.basicConfig(format=fmt)

# Create a dictionary to fill values
d = {'user' : 'rchatterjee'}

# Retrieve the logger
logger = logging.getLogger('sampleLogger')

# Warning message
logger.warning('WARNING: %s', 'There is an unexpected problem.', extra=d)

