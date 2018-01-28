dict = {'Name': 'Ori', 'Age':1, 'Class': 4}

print ("dict ['Name']: ", dict['Name'])
print ("dict['Age']:", dict['Age'])

#修改字典
dict['Age'] = 8
dict['Schoool'] = "FDFZ"

print ("dict['Age']: ",dict['Age'])
print ("dict['School']: ",dict['School'])

#删除
del dict['Name']#删除键
dict.clear()    #清空字典
del dict        #删除字典
