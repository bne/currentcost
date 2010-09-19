
"""Read configuration"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

import logging
import os
import sys

from ConfigParser import ConfigParser
from ConfigParser import NoOptionError
from ConfigParser import NoSectionError

DEFAULTS = {
    'baud': 9600, # Note many people report this being 2400 for them
    'device': '/dev/ttyUSB0',
    'use_meter_time': False,
    'db': 'sqlite',
    'loglevel': 'ERROR',
    'logfile': '/tmp/currentcost.log',
    }

class ConfigError(Exception):
    pass

def start_logger(logfile, loglevel, verbose=False):

    logger = logging.getLogger('currentcost')
    loglevel = getattr(logging, loglevel)
    if verbose:
        hdlr = logging.StreamHandler(sys.stderr)
    else:
        hdlr = logging.FileHandler(logfile)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(loglevel)
    logger.debug('logging system initialised')
    return logger

class Config(object):
    """In which we store our configuration"""
    
    def __init__(self, filename, **kwargs):
        config = ConfigParser(DEFAULTS)
        config.read(filename)
        loglevel = config.get('logging', 'loglevel')
        logfile = config.get('logging', 'logfile', vars=kwargs)
        verbose = kwargs.get('verbose', False)
        self.logger = start_logger(logfile, loglevel, verbose)
        self.device = config.get('system', 'device')
        self.baud = config.get('system', 'baud')
        self.db = config.get('system', 'db')
        self.use_meter_time = config.get('system', 'use_meter_time')
        
