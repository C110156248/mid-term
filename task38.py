n = int(input("小狗有可能跑到的n個地方(2<=n<=10):"))
k = []
for i in range(n):
    k.append(int(input("小明猜想的點與家的距離k(1<=k<=1000:")))
for i in range(len(k)):
    if k[i]%9==0 or k[i]%11==0:
        print("第",str(i+1),"個點", k[i])