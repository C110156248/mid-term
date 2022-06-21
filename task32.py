a = int(input("小明身上有幾元:"))
b = int(input("販賣機有幾種飲料:"))
p = []
z = 0
for i in range(b):
    p.append(input(""))
p = list(map(int, p))
for i in range(len(p)):
    if a >= p[i]:
        z += 1
print(str(z))