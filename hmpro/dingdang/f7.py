f=open('a.txt','a',encoding='utf-8')
data=r"\nwww"
f.write("\n")
f.write(data)

f.close()
print(data)
