import csv
fileHeader=["Glory"]
d1=["no.","name"]
d2=["1","yexiu"]
d3=["2","yuwenzhou"]
d4=["3","huangshaotian"]
d5=["4","wangjiexi"]
csvFile=open("s2.csv","w")
wr=csv.writer(csvFile)
wr.writerows([fileHeader,d1,d2,d3,d4,d5])
csvFile.close()
