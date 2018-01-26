import csv
csvFile = open("demo.csv","r")
reader = csv.reader(csvFile)
for item in reader:
    print(item)
