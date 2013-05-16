import re
import pdb


import pprint
pp = pprint.PrettyPrinter(indent = 4)


from my_books import my_books

print "****************"
print "bbq book manager"
print "****************"

# books i've read

print
print "****************"
print "books i've read"
print "****************"


for b in my_books:
    if b["Reading Status"] == "Read":
        print b["My Rating"], b["Date Read"], b["Title"]

print
print "****************"
print "books on kindle that i want to read"
print "****************"

# books i have on kindle and want to read
for b in my_books:
    if b["Bumps"] > 0 and b["Kindle"] > 0:
        print b["Bumps"], b["Date Added"], b["Title"]
print
print "****************"
print "physical books that i want to read"
print "****************"


# books i physically own and want to read
for b in my_books:
    if b["Bumps"] > 0 and b["Owned"] > 0 and b["Kindle"] <= 0:
        print b["Bumps"], b["Date Added"], b["Title"]

print
print "****************"
print "the great to read list"
print "****************"


# books i want to read and do not own
for b in my_books:
    if b["Bumps"] > 2 and b["Owned"] <= 0:
        print b["Bumps"], b["Date Added"], b["Title"]

  # available on kindle
  # not available on kindle

# bump a book

print
print "****************"
print "books i'm reading"
print "****************"


# books i want to read and do not own
for b in my_books:
    if b["Reading Status"]  =="Reading":
        print b["Bumps"], b["Date Added"], b["Title"]

  # available on kindle
  # not available on kindle

# bump a book


