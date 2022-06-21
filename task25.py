a=input("請輸入考試次數及學生數").split(" ")
b=input("請輸入考試占比").split(" ")
# a="6 3".split(" ")
# b="0.1 0.1 0.3 0.1 0.1 0.3".split(" ")
c=[]
for i in range(len(a)): a[i]=int(a[i])
for i in range(len(b)): b[i]=float(b[i])
if a[0] == len(b):
    for i in range(int(a[1])):
        c.append(input("同學考試分數").split(" "))
else:
    print("輸入錯誤")
d=0
# c.append("70 80 90 80 100 80".split(" "))
# c.append("60 70 80 70 40 70".split(" "))
# c.append("30 50 40 60 50 40".split(" "))
for i in range(a[1]):
    for j in range(a[0]):
        d+=int(c[i][j])*b[j]
d/=a[1]
print("期末考成績為{:.2f}".format(d))