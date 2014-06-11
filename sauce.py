import re
import pdb

import sys

import datetime
import calendar
from dateutil.relativedelta import relativedelta

import pprint
pp = pprint.PrettyPrinter(indent = 4)

width_stars = 35

from db import session
from models import Book

dashes="-"*86

def pretty_counts(when, counts, pages):
    year = when.year
    month = when.month
    tag = str(year) + "-" + str(month)
    n = 0
    if tag in counts:
        n = counts[tag]
    label = str(calendar.month_name[month]).rjust(12) + " " + str(year)
    print str(label).ljust(15), 
    stars = ""
    for i in range(0, n):
        stars += "* "
    print str(stars).ljust(width_stars), str(n).rjust(3),
    if tag in pages:
        print str(pages[tag]).rjust(7)
    else:
        print str("0").rjust(7)


    
def year_analysis(books_read):
    pages = {}
    # how many books read this year?
    counts = {}
    now = datetime.datetime.now()
    for b in books_read:
        if b.date_read is not None:
            tag = b.date_read.year
            if tag in counts:
                counts[tag] += 1
            else:
                counts[tag] = 1
                pages[tag] = 0
            if b.pages is not None:
                if not isinstance(b.pages, unicode):
                    pages[tag] += b.pages
    
    print dashes
    width_pages = 7
    if now.year in counts:
        print str("This year").rjust(12) + " " + str(now.year),
        print str("").ljust(width_stars), str(counts[now.year]).rjust(3),
        print str(pages[now.year]).rjust(width_pages)
    print str("Last year").rjust(12) + " " + str(now.year-1),
    print str("").ljust(width_stars), str(counts[now.year-1]).rjust(3),
    print str(pages[now.year-1]).rjust(width_pages)
    for i in range(now.year-2, 2005, -1):
        print str("").rjust(12) + " " + str(i),
        print str("").ljust(width_stars), str(counts[i]).rjust(3),
        print str(pages[i]).rjust(width_pages)

    


def month_analysis(books_read):
    # let's go back through the last n months
    counts = {}
    pages = {}
    for b in books_read:
        if b.date_read is not None:
            tag = str(b.date_read.year) + "-" + str(b.date_read.month)
            if tag in counts:
                counts[tag] += 1
            else:
                counts[tag] = 1
                pages[tag] = 0
            if b.pages is not None:
                if not isinstance(b.pages, unicode):
                    pages[tag] += b.pages


    now = datetime.datetime.now()
    

    print "books read over time", " "*20, "books", "  pages"
    print dashes
    for less in range(0, 14):
        pretty_counts(now+relativedelta( months = -less ), counts, pages)

    

    

def print_books(books, read=False):
    for b in books:
        print str(b.bumps).rjust(3),
        if read == False:
            print str(b.date_added)[0:10].rjust(12),
        else:
            print str(b.date_read)[0:10].rjust(12),
        unicode_happy = str((b.title).encode('utf-8')[0:49]).ljust(49)
        print unicode_happy,
        print str(b.pages).rjust(5),
        print str(b.isbn_13).rjust(13)
        

def display_books(heading, query_results, limit=10, suppress_count=False, read=False):
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

month_analysis(books_read)

year_analysis(books_read)

print dashes

display_books("books i've recently read", books_read, read=True)

#

books_reading = session.query(Book).filter(Book.status=="Reading").order_by(Book.bumps.desc(), Book.pages.asc()).all()

display_books("books i'm reading", books_reading)

#

books_on_kindle_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==True, Book.status=="To Read").order_by(Book.bumps.desc(), Book.pages.asc()).all()

display_books("books on kindle i own that i want to read",
              books_on_kindle_to_read)

#

books_physical_to_read = session.query(Book).filter(Book.owned==True, Book.kindle==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.pages.asc()).all()

display_books("physical books i own that i want to read",
              books_physical_to_read)

#

books_unowned_to_read = session.query(Book).filter(Book.owned==False, Book.status=="To Read").order_by(Book.bumps.desc(), Book.pages.asc()).all()

display_books("books i want to read and do not own",
              books_unowned_to_read,
              suppress_count=True)

print


