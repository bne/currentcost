
"""Datastore for SQLAlchemy"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Readings(Base):
    """In which we store our readings"""
    
    id = Column(Integer, primary_key=True),
    date_taken = Column(DateTime, nullable=False)
    temperature = Column(Float, precision=1, nullable=False)
    ch1_watts = Column(Integer, nullable=True)
    ch2_watts = Column(Integer, nullable=True)
    ch3_watts = Column(Integer, nullable=True)
    
    def __init__(self, date_taken, temperature, ch1_watts, ch2_watts, ch3_watts):
        """Construct me"""
        self.date_taken = date_taken
        self.temperature = temperature
        self.ch1_watts = ch1_watts
        self.ch2_watts = ch2_watts
        self.ch3_watts = ch3_watts
        

class History(Base):
    """In which we store history"""
    
    id = Column(Integer, primary_key=True)
    reading_id = Column(None, ForeignKey('readings.id'))
    h02 = Column(Float, precision=1, nullable=False)
    h04 = Column(Float, precision=1, nullable=False)
    h06 = Column(Float, precision=1, nullable=False)
    h08 = Column(Float, precision=1, nullable=False)
    h10 = Column(Float, precision=1, nullable=False)
    h12 = Column(Float, precision=1, nullable=False)
    h14 = Column(Float, precision=1, nullable=False)
    h16 = Column(Float, precision=1, nullable=False)
    h18 = Column(Float, precision=1, nullable=False)
    h20 = Column(Float, precision=1, nullable=False)
    h22 = Column(Float, precision=1, nullable=False)
    h24 = Column(Float, precision=1, nullable=False)
    h26 = Column(Float, precision=1, nullable=False)
    d01 = Column(Integer, nullable=False)
    d02 = Column(Integer, nullable=False)
    d03 = Column(Integer, nullable=False)
    d04 = Column(Integer, nullable=False)
    d05 = Column(Integer, nullable=False)
    d06 = Column(Integer, nullable=False)
    d07 = Column(Integer, nullable=False)
    d08 = Column(Integer, nullable=False)
    d09 = Column(Integer, nullable=False)
    d10 = Column(Integer, nullable=False)
    d11 = Column(Integer, nullable=False)
    d12 = Column(Integer, nullable=False)
    d13 = Column(Integer, nullable=False)
    d14 = Column(Integer, nullable=False)
    d15 = Column(Integer, nullable=False)
    d16 = Column(Integer, nullable=False)
    d17 = Column(Integer, nullable=False)
    d18 = Column(Integer, nullable=False)
    d19 = Column(Integer, nullable=False)
    d20 = Column(Integer, nullable=False)
    d21 = Column(Integer, nullable=False)
    d22 = Column(Integer, nullable=False)
    d23 = Column(Integer, nullable=False)
    d24 = Column(Integer, nullable=False)
    d25 = Column(Integer, nullable=False)
    d26 = Column(Integer, nullable=False)
    d27 = Column(Integer, nullable=False)
    d28 = Column(Integer, nullable=False)
    d29 = Column(Integer, nullable=False)
    d30 = Column(Integer, nullable=False)
    d31 = Column(Integer, nullable=False)
    m01 = Column(Integer, nullable=False)
    m02 = Column(Integer, nullable=False)
    m03 = Column(Integer, nullable=False)
    m04 = Column(Integer, nullable=False)
    m05 = Column(Integer, nullable=False)
    m06 = Column(Integer, nullable=False)
    m07 = Column(Integer, nullable=False)
    m08 = Column(Integer, nullable=False)
    m09 = Column(Integer, nullable=False)
    m10 = Column(Integer, nullable=False)
    m11 = Column(Integer, nullable=False)
    m12 = Column(Integer, nullable=False)
    y01 = Column(Integer, nullable=False)
    y02 = Column(Integer, nullable=False)
    y03 = Column(Integer, nullable=False)
    y04 = Column(Integer, nullable=False)

    def __init__(self, history):
        """Constructor - but let's make this easy, eh?"""
        self.__dict__.update(history) # does this work? It might break SQLAlchemy magic
        # Alternative might be:
        # for k, v in history:
        #     setattr(self, k, f)
        
class System(Base):
    """In which we store system"""
    
    did = Column(String(10))
    name = Column(String(10))
    dtype = Column(String(10))
    version = Column(String(10))
    
    def __init__(self, did, name, dtype, version):
        """Constructor"""
        self.did = did
        self.name = name
        self.dtype = dtype
        self.version = version
        
