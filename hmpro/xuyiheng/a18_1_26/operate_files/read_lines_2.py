f = open('notes.txt','r',encoding='utf-8')
content = f.readlines()
print('readlines: ',content)
f.close
