a=input("請輸入純數字(誤有空格)")
dp=[]
b=len(a)
num=0
ans=[]
c=[]
d=0
for j in range(b,0,-1):
    for i in range(j):
        dp.append(a[i:j])
for x in range(len(dp)):
    if dp[x] == dp[x][::-1]:
        ans.append(int(dp[x]))
        
        
print(max(ans))