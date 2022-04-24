a=input("請輸入一個數字列(用空格隔開)")
b=a.split(" ")
c=[]
d=0
e=""
for i in range(len(b)):
    d=0
    if b.count(b[i])>len(b)/2 and b[i] not in c:
        c.append(b[i])
for x in range(len(c)):
    e+=c[x]
if e=="":
    print("過半元素為:NO")
else:
    print("過半元素為:%s"%(e))