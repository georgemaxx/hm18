import csv
csvFile = open("demo.scv","r")
reader = csv.reader(csvFile)
for item in reader:
    print(item)
