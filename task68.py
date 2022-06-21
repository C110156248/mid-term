x=list(input('請輸入第一組數字：'))
y=list(input('請輸入第二組數字：'))
while True:
    a=0
    b=0
    for i in range(len(x)):
        if x[i]==y[i]:
            a+=1
        else:
            b+=1
    if a==len(x):
        print("%dA%dB" %(a,b)+'全對')
        break
    else:            
        print("%dA%dB" %(a,b)+'加油')
        y=list(input('請輸入第二組數字：'))