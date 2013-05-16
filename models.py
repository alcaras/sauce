from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, BigInteger, Boolean, Integer, String, DateTime, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

import string
import pdb

#try:
#    from app import db
#    Base = db.Model           # for use with flask
#except ImportError:

Base = declarative_base() # for use without flask (e.g. cronjobs)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    
    title = Column(String)
    author = Column(String)
    author_extra = Column(String)
    publisher = Column(String)
    isbn = Column(String)
    isbn_13 = Column(String)
    my_rating = Column(Integer)
    date_read = Column(DateTime)
    date_added = Column(DateTime)
    review = Column(String)
    bumps = Column(Integer)
    status = Column(String)
    owned = Column(Boolean)
    kindle = Column(Boolean)
        
