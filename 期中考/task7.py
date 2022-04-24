# a=input("請輸入月租費形式及通話時間為(用逗號隔開)")
a="386,36000"
b=a.split(",")
tie=0
if b[0]=="186":
    tie=int(b[1])*0.08
    if tie<=int(b[0]):
        print("通話費為0")
    elif tie-int(b[0])>int(b[0]):
        tie*=0.8
        print("通話費為%d"%(tie+1))
    elif tie-int(b[0])<=int(b[0]):
        tie*=0.9
        print("通話費為%d"%(tie+1))
elif b[0]=="386":
    tie=int(b[1])*0.08
    if tie<=int(b[0]):
        print("通話費為0")
    elif tie-int(b[0])>int(b[0]):
        tie*=0.7
        print("通話費為%d"%(tie+1))
    elif tie-int(b[0])<=int(b[0]):
        tie*=0.8
        print("通話費為%d"%(tie+1))
elif b[0]=="586":
    tie=int(b[1])*0.07
    if tie<=int(b[0]):
        print("通話費為0")
    elif tie-int(b[0])>int(b[0]):
        tie*=0.6
        print("通話費為%d"%(tie+1))
    elif tie-int(b[0])<=int(b[0]):
        tie*=0.7
        print("通話費為%d"%(tie+1))
    
elif b[0]=="986":
    tie=int(b[1])*0.06
    if tie<=int(b[0]):
        print("通話費為0")
    elif tie-int(b[0])>int(b[0]):
        tie*=0.5
        print("通話費為%d"%(tie+1))
    elif tie-int(b[0])<=int(b[0]):
        tie*=0.6
        print("通話費為%d"%(tie+1))