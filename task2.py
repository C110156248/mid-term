a=525
b=0
c=0
if a<=120:
    b=120*2.1
    c=120*2.1
    print("summer months"+b)
    print("non-summer months"+c)
elif 331>a>120:
    b=120*2.1+(a-120)*3.02
    c=120*2.1+(a-120)*2.68
    print("summer months"+b)
    print("non-summer months"+c)
elif 501>a>330:
    b=120*2.1+210*3.02+(a-330)*4.39
    c=120*2.1+210*2.68+(a-330)*3.61
    print("summer months"+b)
    print("non-summer months"+c)
elif 701>a>500:
    b=120*2.1+210*3.02+170*4.39+(a-500)*4.97
    c=120*2.1+210*2.68+170*3.61+(a-500)*4.01
    print("summer months"+b)
    print("non-summer months"+c)
else:
    b=120*2.1+210*3.02+170*4.39+200*4.97+(a-700)*5.63
    c=120*2.1+210*2.68+170*3.61+200*4.01+(a-700)*4.5
    print("summer months"+b)
    print("non-summer months"+c)