from os import remove

x=input('輸入自傳(至少10字)')
l=[]
for i in x:
    y=x.count(i,0,len(x))
    if y>1 and i not in l:
        l.append(i)
if '，' in l:
    l.remove('，')
if '。' in l: 
    l.remove('。')
if ',' in l:
    l.remove(',')
print(l)   