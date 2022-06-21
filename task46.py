n = int(input("輸入筆數n:"))
d = {}
for i in range(n):
    x,y=input("").split()
    x=str(x);y=int(y)
    d[x]=y
for x , y in d.items():
    print("%s牌得到%d面"%(x,y))