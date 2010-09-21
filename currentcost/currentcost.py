
"""Let's talk"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

from decimal import Decimal
from xml.etree import ElementTree # This will go wrong in early pythons...
from xml.parsers.expat import ExpatError

import serial

class JunkData(Exception):
    pass

class IncompleteData(JunkData):
    pass

class WrongBaudRate(JunkData):
    pass

class CurrentCost(object):
    """Let's talk to the current cost"""
    
    def __init__(self, config=None):
        self.baud = 9600
        self.device = '/dev/ttyUSB0'
        self.timeout = 1
        self.use_meter_time = False
        self.verbose = True
        if config is not None:
            self.baud = config.baud
            self.device = config.device
            self.use_meter_time = config.use_meter_time
        try:
            self.s = serial.Serial(self.device, self.baud, timeout=self.timeout)
        except:
            raise
        
    def system(self):
        return self.getdata()['system']
    
    def history(self):
        return self.getdata()['history']
    
    def temperature(self):
        return self.getdata()['temperature']
    
    def power(self):
        """This assumes that, like almost all installations, users are only
        interested in the power output from channel 1"""
        return self.getdata()['channels'][0]
    
    def getdata(self):
        et = self.loadxml()
        data = self._processdata(et)
        return data
    
    def loadxml(self):
        xml = self.s.readline()
        try:
            # number of failure possibilities:
            #  * First call to the device may return only part of a string
            #  * Wrong baud rate returns gibberish
            #  * Occassionally we get nothing at all ('')
            # XXX: I think some of these are wrong...
            et = ElementTree.fromstring(xml)
        except ExpatError, e:
            if e.code == 2:
                raise IncompleteData("Only received part of a string - try again")
            if e.code == 3:
                raise IncompleteData("Got the empty string - try again")
            if e.code == 4:
                raise WrongBaudRate("Got gibberish - try a different baud rate")
            raise JunkData(e.message)
        if self.verbose:
            print ElementTree.tostring(et)
        return et
        
    def _processdata(self, et):
        """Take a(n already parsed) valid message from the meter and
        return a data structure"""
        d = {
            'days_since_birth': int(et.find('date/dsb').text),
            'meter_time': ':'.join([ e.text for e in et.find('date')[1:] ]),
            'system': {
                'name': et.find('src/name').text,
                'id': et.find('src/id').text,
                'type': et.find('src/type').text,
                'software_version': et.find('src/sver').text,
                },
            'channels': [
                int(et.find('ch1/watts').text),
                int(et.find('ch2/watts').text),
                int(et.find('ch3/watts').text),
                ],
            'temperature': Decimal(et.find('tmpr').text),
            'history': {
                'hours': dict([ (e.tag[1:], Decimal(e.text)) for e in et.find('hist/hrs') ]),
                'days': dict([ (e.tag[1:], int(e.text)) for e in et.find('hist/days') ]),
                'months': dict([ (e.tag[1:], int(e.text)) for e in et.find('hist/mths') ]),
                'years': dict([ (e.tag[1:], int(e.text)) for e in et.find('hist/yrs') ]),
                },
            }
        return d
    