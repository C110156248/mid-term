x=int(input('輸入金額:'))
hun=x//100
fif=x%100//50
ten=x%100%50//10
fiv=x%100%50%10//5
one=x%100%50%10%5
ans=hun+fif+ten+fiv+one
print(ans)