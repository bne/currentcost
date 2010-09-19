
"""Let's talk"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

import serial

class CurrentCost(object):
    """Let's talk to the current cost"""
    
    def __init__(self, config=None):
        self.baud = 9600
        self.device = '/dev/ttyUSB0'
        self.timeout = 1
        if config is not None:
            self.baud = config.baud
            self.device = config.device
        try:
            self.s = serial.Serial(self.device, self.baud, self.timeout)
        except:
            raise
        
    def readline(self):
        return self.s.readline()
    
    def readlines(self):
        return self.s.readlines()
    
