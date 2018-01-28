#{}字典
citys = {
     '上海':{
     '浦东':['东方明珠','金茂大厦','上海中心'],
     '杨浦',
     '宝山'
     '徐汇'
     '徐浦'
     }
     '北京':{
     '朝阳',
     '海淀',
     '昌平',
     '怀柔',
     '密云'
     }
}

for i in citys['北京']:
      print (i)

for i in citys['上海']['浦东']:
      print(i)


程序2
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
#k,v指代两个变量，可改为其他的。目的是分别反应键和值
