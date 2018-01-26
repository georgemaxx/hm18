import csv
fileheader = ["name","score"]
d1 = ["wang","100"]
d2 = ["li","80"]
csvFile = open("sheet.csv","w",encoding = "utf_8")
writer = csv.writer(csvFile)
writer.writerow(fileheader)
writer.writerow(d1)
writer.writerow(d1)
csvFile.close()
