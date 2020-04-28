import pandas as pd
import csv
import os

DIR = "Data"
encoding = 'utf-16'

with open('comments.csv', 'w', encoding=encoding, newline='\n') as csv_file:
    writer = csv.writer(csv_file)
    for root, dirs, files in os.walk(DIR):
        i = 1
        writer.writerow(["Index", "Content", "Sentiment"])
        for f in files:
            with open(os.path.join(root, f), 'r', encoding=encoding) as fo:
                content = fo.read()
                #content.decode(encoding)
                #content.decode('utf8')
                print(content)
                writer.writerow([i, content, 0])
            print(i)
            i += 1


class CSVWriter():

    filename = None
    fp = None
    writer = None

    def __init__(self, filename):
        self.filename = filename
        self.fp = open(self.filename, 'w', encoding='utf8')
        self.writer = csv.writer(self.fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def close(self):
        self.fp.close()

    def write(self, elems):
        self.writer.writerow(elems)

    def size(self):
        return os.path.getsize(self.filename)

    def fname(self):
        return self.filename

""" 
mycsv = CSVWriter('/tmp/test.csv')
mycsv.write((12,'green','apples'))
mycsv.write((7,'yellow','bananas'))
mycsv.close()
print("Written %d bytes to %s" % (mycsv.size(), mycsv.fname())) 
"""