a=input("請輸入純數字(誤有空格)")
dp=[]
b=len(a)
num=0
ans=[]
for j in range(b,0,-1):
    for i in range(j):
        dp.append(a[i:j])

for x in range(len(dp)):
    if int(dp[x])/2 != 0:
        for y in range(1,int(dp[x])+1):
            if int(dp[x])%y==0:
                num+=1
            if num>2:
                break
        if num==2:
            ans.append(dp[x])
            num=0
        else:
            num=0
if ans!="":
    print(max(ans))
else:
    print("no prime found")