n = int(input("輸入筆數n:"))
l = []
for i in range(n):
    x = input().split()
    l.append(x)
for i in range(n):
    print(l[i][0],"牌得到",l[i][1],"面")