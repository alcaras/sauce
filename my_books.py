import cPickle as pickle

jar = open('books.pickle', 'rb')
my_books = pickle.load(jar)
jar.close()
