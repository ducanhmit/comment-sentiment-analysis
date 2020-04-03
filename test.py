import csv

with open('comments.csv', 'r', encoding='utf-16') as file:
    reader = csv.reader( (line.replace('\0','') for line in file) )
    for row in reader:
        print(row)