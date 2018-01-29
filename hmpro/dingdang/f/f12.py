import csv
csvFile=open("s1.csv","r")
reader=csv.reader(csvFile)
for item in reader:
    print(item)
