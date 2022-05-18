# a=input("輸入4個數字")
a="1234"
b=[]
for i in a:
    b.append(str((int(i)+7)%10))
c=b[2]+b[3]+b[0]+b[1]
print(c)