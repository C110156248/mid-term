a = input("輸入題目(四位數):")
ans = []
for i in range(4):
    ans.append(a[i])

while True:
    A = 0
    B = 0
    aq = []
    q = input("輸入四位數:")
    if q == '0000':
        print("結束")
        break
    for i in range(4):
        aq.append(q[i])
    for i in range(4):
        if aq[i] == ans[i]:
            A += 1
        elif aq[i] != ans[i] and aq[i] in ans:
            B += 1
    print('%dA%dB' % (A, B))
    if A == 4:
        break