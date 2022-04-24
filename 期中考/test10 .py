a=input("輸入n及m(矩陣大小)")
b=a.split(" ")
c=[]
d=[]
e=""
f=[]
for i in range(int(b[0])):
    c.append(input("請輸入第%d列請輸入%s個數字(用空格隔開)" %(i+1,b[1])))
for j in range(len(c)):
    d.append(c[j].split(" "))
for x in range(int(b[1])):
    for y in range(int(b[0])):
        e+="%s "%(d[y][x])
    f.append(e)
    e=""
for z in range(len(f)):
    print("輸出矩陣數值第%s為%s" %(int(z)+1,f[z]))