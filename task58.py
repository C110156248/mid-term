a = []
for i in range(1,11):
    a.append(int(input('請輸入第%d個數字:'%(i))))
a.sort()
a.reverse()
print('最小的3個數字為:%d,%d,%d' %(a[0],a[1],a[2]))
a.reverse()
print('最大的3個數字為:%d,%d,%d' %(a[0],a[1],a[2]))