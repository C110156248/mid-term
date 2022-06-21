x=int(input("共T筆測試資料(1<=T<=20):"))
for i in range(x):
    y=[]
    a=0
    for j in range(0,4):
        y.append(int(input()))
    if y[1]-y[0]==y[2]-y[1]==y[3]-y[2]:
        y.append(y[3]+y[3]-y[2])
        for i in range(len(y)):
         print("%d"%(y[i]),end=" ")
        print("\n此為等差數列")
    elif y[1]/y[0]==y[2]/y[1]==y[3]/y[2]:
        y.append(y[3]*y[2]/y[1])
        for i in range(len(y)):
         print("%d"%(y[i]),end=" ")
        print("\n此為等比數列")
    else:
        print('這不是數列')