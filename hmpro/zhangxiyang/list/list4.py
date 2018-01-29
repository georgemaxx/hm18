list = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
list2 = []
for j in range(4):
    k = []
    for i in list:
        k.append(i[j])
    list2.append(k)
print(list2)
