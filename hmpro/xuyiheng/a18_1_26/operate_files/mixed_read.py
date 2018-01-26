f = open('notes.txt','r',encoding='utf-8')
data1=f.read(8)
data2=f.readline()
data3=f.read()
f.close
print(data1)
print(data2)
print(data3)
