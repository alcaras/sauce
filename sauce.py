import re
import pdb

import sys

import datetime

import pprint
pp = pprint.PrettyPrinter(indent = 4)


from db import session
from models import Book

dashes="-"*80

def print_books(books, read=False):
    for b in books:
        print str(b.bumps).rjust(3),
        if read == False:
            print str(b.date_added)[0:10].rjust(12),
        else:
            print str(b.date_read)[0:10].rjust(12),
        print str(b.title[0:49]).ljust(49), str(b.isbn_13).rjust(13)
        

def display_books(heading, query_results, limit=7, suppress_count=False, read=False):
    print
    if not suppress_count:
        print heading + " (" + str(len(query_results)) + ")"
    else:
        print heading
    print dashes
    print_books(query_results[0:limit], read)


print "sauce book manager"
print dashes

books_read = session.query(Book).filter(Book.status=="Read").order_by(Book.date_read.desc()).all()

display_books("books i've recently read", books_read, read=True)

#

books_reading = session.query(Book).filter(Book.status=="Reading").order_by(Book.bumps.desc(), Book.date_added.asc()).all()

display_books("books i'm reading", books_reading)

#

books_on_kindle_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==True, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).all()

display_books("books on kindle that i want to read",
              books_on_kindle_to_read)

#

books_physical_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).all()

display_books("physical books that i want to read",
              books_physical_to_read)

#

books_unowned_to_read = session.query(Book).filter(Book.owned==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.date_added.asc()).all()

display_books("books i want to read and do not own",
              books_unowned_to_read,
              suppress_count=True)

print


