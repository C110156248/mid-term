x = int(input("請輸入一個正整數(<=10):"))
for i in range(x):
    y = i+1
    for j in range(i+1):
        print(y,end=" ")
        y += i+1  
    print()