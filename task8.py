m=input("輸入一個數字")
s=input("輸入一個數列(數字間用空格隔開，數值不得大於數字個數)")
p=[]
c=[]
b=1
ans=0
for i in range(len(s)):
    if s[i]!=" ":
        p.append(int(s[i]))
for j in range(1,len(p)+1):
    c.append(p.count(j))
    if p.count(j)>b:
        b=p.count(j)
        ans=p[j]

if max(c)==1:
    print("每個數字都出現1次")
else:
    print("最大出現次數的數字為:%s"%(ans))
    print("出現次數為:%s"%(b))