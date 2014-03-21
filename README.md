# sauce
=====

book organizer/reading list generator using goodreads


## Setup

You'll need to create a credentials.py with two lines:

    user = "you@goodreads.com"
    pass = "your goodreads password"

(Sadly the Goodreads API doesn't provide bulk CSV download, 
as far as I can tell, so we have to log in as you and 
download the CSV file ourselves).


You'll also need to create the database:

    python db_create.py
    
## Updating your DB and Viewing Your Reading List

    ./refresh
    
## Viewing Your Reading List

    ./view
