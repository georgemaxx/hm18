a = 1
def b():
    d=2
    print (d)
    global a
    print (a)
    return a
c = b()
print (c)
