import pprint
pp = pprint.PrettyPrinter(indent = 4)
import csv
import re
import pdb
import cPickle as pickle

from dateutil import parser

from db import session
from models import Book

books = []

print "Reading CSV..."
with open('goodreads_export.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    i = 0
    for row in spamreader:
        if i == 0:
            i += 1
            continue
        book = {}
        book["Title"] = unicode(row[1], 'utf-8')
        book["Author"] = unicode(row[2], 'utf-8')
        book["Extra Author"] = unicode(row[4], 'utf-8')
        book["Publisher"] = unicode(row[9], 'utf-8')
        book["ISBN"] = re.match('="([\d\w]*)"', row[5]).group(1)
        book["ISBN13"] = re.match('="([\d\w]*)"', row[6]).group(1)
        book["My Rating"] = row[7]
        if row[14] == "":
            book["Date Read"] = None
        else:
            book["Date Read"] = parser.parse(row[14])
        book["Date Added"] = parser.parse(row[15])
        book["Review"] = unicode(row[19], 'utf-8')

        book["Bumps"] = 0
        book["Reading Status"] = ""
        if row[18] == "to-read":
            book["Reading Status"] = "To Read"
            book["Bumps"] = 1
        if row[18] == "currently-reading":
            book["Reading Status"] = "Reading"
        if row[18] == "read":
            book["Reading Status"] = "Read"
        book["Owned"] = False
        if "i-own" in row[16]:
            book["Owned"] = True
        book["Kindle"] = False
        if "kindle" in row[16]:
            book["Kindle"] = True

        for i in range(2,9):
            if "-"+str(i) in row[16]:
                book["Bumps"] = i
        books += [book]
    

print "Clearing old database..."
qbooks = session.query(Book).all()
for qb in qbooks:
    session.delete(qb)

print "Importing into DB..."

for book in books:
    new_book = Book(title=book["Title"],
                    author=book["Author"],
                    author_extra=book["Extra Author"],
                    publisher=book["Publisher"],
                    isbn=book["ISBN"],
                    isbn_13=book["ISBN13"],
                    my_rating=book["My Rating"],
                    date_read=book["Date Read"],
                    date_added=book["Date Added"],
                    review=book["Review"],
                    bumps=book["Bumps"],
                    kindle=book["Kindle"],
                    owned=book["Owned"],
                    status=book["Reading Status"],
                    )
    session.add(new_book)

session.commit()

print "Import complete!"
