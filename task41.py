
x = int(input("搭了幾次電梯:"))
k = 1
m = 0 
for i in range(x):
    y = int(input(""))
    while (k == y):
        print("這裡就是%d樓"%(k))
        y = int(input(""))
    else:
        if (y > k):
            m += (y-k)*20
        elif (y < k):
            m += (k-y)*10
    k = y
print("%d 元" %(m))