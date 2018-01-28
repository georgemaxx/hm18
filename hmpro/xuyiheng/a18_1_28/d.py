a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2,-1) #在第二个位置插入-1
print(a)
a.append(333)#在末尾添加
print(a)
a.index(333)
print(a)
a.remove(333)#查找333的下标（第一个是0，第二个是1，以此类推）
print(a)
a.reverse()#从后往前输出
print(a)
a.sort()#从小到大排列
print(a)
