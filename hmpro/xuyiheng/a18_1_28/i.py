#集合

a = {x for x in 'abracadabra' if x not in 'abc'}
#得到a = {'r', 'd'}


#遍历技巧
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
#k,v指代两个变量，可改为其他的。目的是分别反应键和值

#遍历技巧
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket))   #sorted()排序，按照首字母顺序排序
    print (f)
