n = int(input("輸入筆數n:"))
d = {}
for i in range(n):
    x,y = input().split()
    d[x] = y
f = input("輸入欲查詢單字:")
if f in d:
    print(f,"中文意思為",d[f])
else:
    print("字典未有此單字")