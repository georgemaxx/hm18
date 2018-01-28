#列表推倒式

vec = [2,4,6]
[3*x for x in vec]
#会得到[6,12,18]

vec = [2,4,6]
[3*x for x in vec if x > 3]
#会得到[12,18]




[[x,x**2] for x in vec]
#得到[[2,4],[4,16],[6,36]]

#逐个调用序列中的元素
freshfruit = [' banana ', ' loganberry ', ' passion fruit ']
[weapon.strip() for weapon in freshfruit]
#得到的每一个元素都去掉了空格

vec1= [2,4,6]
vec2= [3,5,7]
[x*y for x in vec1 for y in vec2]

[vec1[i]*vec2[i] for i in range(len(vec1))]
#range(x),程序执行x次
#len(vec1) 即vec1的长度（长度为3）
