n = int(input("請輸入查詢組數N為:"))
data ={'123':'456','456':'789','789':'888','336':'558','775':'666','566':'221'}
mon = {'456':9000,'789':5000,'888':6000,'558':10000,'666':12000,'221':7000}

for i in range(n):
    a,p = input("請輸入帳密 (並以空白隔開)").split()
    if p == data[a] :
        print(mon[p])
    else:
        print("ERROR")