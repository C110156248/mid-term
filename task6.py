a=input("輸入一個數(用逗點分開)")
b=a.split(",")
c=sorted(b)
d=sorted(b,reverse=True)
bn=""
sn=""
for i in range(len(b)):
    bn+=d[i]
    sn+=c[i]
print("最大數和最小數差額為%s"%(int(bn)-int(sn)))