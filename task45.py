m = int(input("月"))
d = int(input("日"))
x = (m*2+d)%3
if x == 0:
    print("普通")
elif x == 1:
    print("吉")
elif x == 2:
    print("大吉")