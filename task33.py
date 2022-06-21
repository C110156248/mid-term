a = ["國文","英文","微積分","體育","程式設計"]
b = []
for i in range(len(a)):
    b.append(int(input(a[i]+":")))
print("平均分數:%.2f分" %(sum(b)/len(a)))
print("最高分科目：" + a[b.index(max(b))],max(b),"分")
print("最低分科目：" + a[b.index(min(b))],min(b),"分")