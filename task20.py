# a=input("組數為")
a=3
for i in range(int(a)):
    b=input("第%s組，票種請用空格隔開"%(i+1))
    c=b.split(" ")
    ans=int(c[0])*250+int(c[1])*175
    print("第%s組應收費:%s"%(i+1,ans))