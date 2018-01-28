#列表推倒式

vec = [2,4,6]
[3*x for x in vec]
#会得到[6,12,18]

[[x,x**2] for x in vec]
#得到[[2,4],[4,16],[6,36]]

#逐个调用序列中的元素
freshfruit = [' banana ', ' loganberry ', ' passion fruit ']
[weapon.strip() for weapon in freshfruit]
#得到的每一个元素都去掉了空格
