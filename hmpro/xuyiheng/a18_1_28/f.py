#将列表当做队列使用（第一个加入的元素第一个取出来）
#堆栈：最后加入到元素第一个取出

from collections import deque
queue = deque(['Eric','John','Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()#删除第一个
