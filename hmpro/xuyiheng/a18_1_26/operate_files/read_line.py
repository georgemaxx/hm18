f = open('notes.txt','r',encoding='utf-8')
content = f.readline()
print('readline: ', content.strip())  #strip去掉空格、制表符、换行符
content2 = f.readline()
print(content2.strip())
f.close()
