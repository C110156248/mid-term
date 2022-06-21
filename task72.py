n = int(input("請輸入n:"))
k = int(input("請輸入k:"))
x = n
y = 0
while True:
    y = y + (n//k)
    n = n//k
    if n < k:
        break
print("Peter可以抽",x+y,'支紙菸')