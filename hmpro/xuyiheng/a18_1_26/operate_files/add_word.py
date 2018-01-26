f = open('first.txt','a',encoding='utf-8')
data = r"\noooooooooooooooooooooooooooooo"
f.write(data)
f.close()
print (data)
#\n表示换行，加r正常输入/n
