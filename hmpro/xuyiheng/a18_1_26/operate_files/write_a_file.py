f = open('first.txt','w',encoding='utf-8')
data = "一只慵懒的猫"
f.write(data)
f.close()
print (data)

#“r”只读，“w”只写，会清空原内容，无对象文件会创建，“a”追加写模式
