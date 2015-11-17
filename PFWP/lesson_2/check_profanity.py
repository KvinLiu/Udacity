def read_text():
    quotes = open("/Users/KevinL/Dropbox/Udacity/PFWP/lesson_2/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
