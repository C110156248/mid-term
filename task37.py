n=int(input("整數n:"))
print("數列:",n,end=' ')
while True:
    if n%2==1:
        n=n*3+1
        print("%d"%(n),end=' ')
    elif n%2==0:
        n=n/2
        print("%d"%(n),end=' ')
    if n==1:
        break      