import csv
csvFile = open("target.csv","r",encoding='utf-8')
reader = csv.reader(csvFile)
for item in reader:
    print(item)
