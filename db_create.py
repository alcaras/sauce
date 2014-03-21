from migrate.versioning import api
from db import engine, session
from models import Book
import os.path
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Book.metadata.create_all(engine)

 
