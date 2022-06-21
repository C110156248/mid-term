
x = input("甲方的數字:")
y = input("乙方的數字:")
ans = ''
for i in range(len(x)):
    if x[i] == '1' and y[i] == '5':
        ans += '贏'
    elif x[i] == '2' and y[i] == '1':
        ans += '贏'
    elif x[i] == '3' and y[i] == '2':
        ans += '贏'
    elif x[i] == '4' and y[i] == '3':
        ans += '贏'
    elif x[i] == '5' and y[i] == '4':
        ans += '贏'
    elif x[i] == '1' and y[i] == '2':
        ans += '輸'
    elif x[i] == '2' and y[i] == '3':
        ans += '輸'
    elif x[i] == '3' and y[i] == '4':
        ans += '輸'
    elif x[i] == '4' and y[i] == '5':
        ans += '輸'
    elif x[i] == '5' and y[i] == '1':
        ans += '輸'
    else:
        ans += '和'
print(ans)