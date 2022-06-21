a = int(input("輸入一正整數:"))
if a % 2 == 0 and a % 11 == 0:
    if a % 5 != 0 and a % 7 != 0:
        print("%d為新公倍數?:Yes" % (a))
else:
    print("%d為新公倍數?:No" % (a))