# login as me and then
# http://www.goodreads.com/review_porter/goodreads_export.csv

import mechanize
import cookielib
import datetime
import urllib2
import sys

from credentials import user, password

csv_url = "http://www.goodreads.com/review_porter/goodreads_export.csv"
filename = "goodreads_export.csv"

# override mechanize's history behavior
class NoHistory(object):
  def add(self, *a, **k): pass
  def clear(self): pass


# Browser
br = mechanize.Browser(factory=mechanize.RobustFactory(), history=NoHistory())

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

dt = datetime.datetime

# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1')]

try:
    print dt.now(), "grab_csv: Attempting to log in..."
    r = br.open('http://goodreads.com/')
    html = r.read()
    
    br.select_form(nr=0)
    br.form['user[email]'] = user
    br.form['user[password]'] = password
    br.submit()
except urllib2.HTTPError, e:
    print dt.now(), e.code
    sys.exit()

print dt.now(), "grab_csv: Successfully signed in."

print dt.now(), "grab_csv: Getting CSV...",

r = br.open(csv_url)
csv = r.read()

print "done."

print dt.now(), "grab_csv: Writing to", filename, "...",

f = open(filename, 'w')
f.write(csv)
f.close()

print "done."





