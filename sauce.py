import re
import pdb

import sys

import pprint
pp = pprint.PrettyPrinter(indent = 4)


from db import session
from models import Book


def print_books(books):
    for b in books:
        print str(b.bumps).rjust(3), str(b.date_added)[0:10].rjust(12),
        print str(b.title[0:49]).ljust(49), str(b.isbn_13).rjust(13)
        

limit = 7
dashes = "-"*80

print "sauce book manager"
print dashes

print
print "books on kindle that i want to read"
print dashes


# this should really be sorted by bumps, date_added
# the proper way to do this is just import into a db

books_on_kindle_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==True, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).limit(limit).all()

print_books(books_on_kindle_to_read)

print
print "physical books that i want to read"
print dashes

books_physical_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).limit(limit).all()

print_books(books_physical_to_read)


print
print "books i want to read and do not own"
print dashes


books_unowned_to_read = session.query(Book).filter(Book.owned==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).limit(limit).all()

print_books(books_unowned_to_read)


print
print "books i'm reading"
print dashes


books_reading = session.query(Book).filter(Book.status=="Reading").order_by(Book.bumps.desc(), Book.date_added.asc()).limit(limit).all()

print_books(books_reading)
