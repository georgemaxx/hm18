import csv
fileHeader = ["name","score"]
d1 = ["Wang","100"]
d2 = ["Li","80"]
csvFile = open("instance.csv","w")
writer = csv.writer(csvFile)
writer.writerow(fileHeader)
writer.writerow(d1)
writer.writerow(d2)
csvFile.close
#writer.writerow([fileHeader, d1, d2])
