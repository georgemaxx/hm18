import csv
csvfile = open("sheet.csv","r",encoding = "utf-8")
reader = csv.reader(csvfile)
for item in reader:
    print(item)
