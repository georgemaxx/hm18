def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   #插入的是次级列表
   #"."表示调用append函数
   for i in range(3):
      mylist.append(i+1)
   #插入的是单个元素
   print ("函数内取值：",mylist)
   return

mylist=[10,20,30]
changeme( mylist )
print("函数外取值：", mylist)
