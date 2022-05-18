ans=[]
# a1=input("輸入矩陣大小中間以空格隔開")
a1="2 2"
b1=a1.split(" ")
c1=[]
d1=[]
# for i in range(int(b1[0])):
    # c1.append(input("請輸入矩陣內容空格隔開"))
c1.append("1 2")
c1.append("3 4")
for j in range(len(c1)):
    d1.append(c1[j].split(" "))

# a2=input("輸入矩陣大小中間以空格隔開")
a2="2 2"
b2=a2.split(" ")
c2=[]
d2=[]
# for i in range(int(b2[0])):
    # c2.append(input("請輸入矩陣內容空格隔開"))
c2.append("5 6")
c2.append("7 8")
for j in range(len(c2)):
    d2.append(c2[j].split(" "))

if b1[0]==b2[0] and b1[1]==b2[1]:
    for x in range(len(c1)):
        for y in range(len(d1)):
            ans.append(int(d1[x][y])+int(d2[x][y]))
    print(ans)
else:
    print("兩陣列不能相加")
