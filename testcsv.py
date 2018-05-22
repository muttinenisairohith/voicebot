import csv
file = open('dbc.csv',"rb")
reader = csv.reader(file)
for row in reader:

