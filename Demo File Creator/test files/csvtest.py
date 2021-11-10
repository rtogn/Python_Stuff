import csv
csvfile = open('Demo.csv','r')
reader = csv.reader(csvfile, delimiter=',', quotechar-'"')
for line in csvfile:
    row = line.split(",")
    print(row[1])
