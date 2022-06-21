a = input("請輸入A的好友:").split()
b = input("請輸入B的好友:").split()
x = 0
for i in range(len(a)):
    if a[i] in b:
        x += 1
print(x)