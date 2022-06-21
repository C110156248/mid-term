a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
x=b**2-4*a*c
if x>0:
    x1=(-b + x**0.5) / 2*a
    x2=(-b - x**0.5) / 2*a
    print("%d\n%d"%(x1,x2))
elif x==0:
    x1=-b/2*a
    print(int(x1))
elif x<0:
    print(0)