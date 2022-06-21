a=True
while a==True:
    b=input("檢測的字串")
    if b == "end":
        print("檢測結束")
        break
    else:
        c=input("檢測的單一字元")
        print(b.count(c))
