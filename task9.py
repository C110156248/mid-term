a=input("請輸入兩個字串用逗點隔開")
b=a.split(",")
if b[0] in b[1]:
    print("yes")
else:
    print("no")