import csv
from urllib.request import urlopen

url = 'http://winterolympicsmedals.com/medals.csv'
response = urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

for row in cr:
    print (row)