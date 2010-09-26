
"""Base classes for readers"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

class JunkData(Exception):
    pass

class IncompleteData(JunkData):
    pass

class WrongBaudRate(JunkData):
    pass

class ReaderWrapper(object):
    """So we can use 'with'"""
    def __init__(self, klass, **kwargs):
        self.klass = klass
        self.kwargs = kwargs
        
    def __enter__(self):
        """Create an instance of klass and return it"""
        self.reader = self.klass(**self.kwargs)
        return self.reader
    
    def __exit__(self, type, value, tb):
        """Ensure comms are shut down correctly"""
        self.reader.close()
        
class BaseReader(object):
    """I have been muttering to myself about zope.interface, but it
    introduces a dependency and without adaptation feels like overkill"""
    
    def close(self):
        """Stop communications"""
        pass
        
    def open(self):
        """Start communications"""
        pass
        
    def __iter__(self):
        """Iterable"""
        pass
            
    def system(self):
        """Return system information about the device. May return None"""
        pass
    
    def history(self):
        """Return historical information from the device of the form:
        {'hours': {'h02':..., ..., 'h26'},
         'days': ,
         'months': ,
         'years': ,
          }
        """
        #XXX not very generic...
        pass
    
    def temperature(self):
        """Return the current temperature.  May return None"""
        pass
    
    def power(self):
        """Return the default power reading from the device (i.e. channel 1 in most cases)"""
        pass
    
    def getdata(self):
        """Return the full data structure available"""
        pass
