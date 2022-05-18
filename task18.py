a=[]
for i in range(5):
    a.append(input("輸入卡值"))
b=0
for j in range(len(a)):
    if a[j]=="A":
        b+=1
    elif a[j]=="J":
        b+=11
    elif a[j]=="Q":
        b+=12
    elif a[j]=="K":
        b+=13
    else:
        b+=int(a[j])
print(b)