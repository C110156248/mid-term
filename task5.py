# a=input("輸入一個數")
a=1000
b=1
c=0
def cal(c):
    cal=1
    for i in range(1,c+1):
        cal*=i
    return cal

while True:
    c=cal(b)
    if c>a:
        break
    else:
        b+=1
print(b)