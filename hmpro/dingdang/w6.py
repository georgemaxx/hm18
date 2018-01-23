def printinfo(arg1,*vartuple):
    print("本局金币数/经验值：")
    print(arg1)
    for var in vartuple:
        print(var)
    return;
printinfo(50);
printinfo(200,20);
printinfo(370,240);
