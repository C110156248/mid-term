import random
id=[]
name="C1101562"
for j in range(0,51):
    id.append(name+"{0:02d}".format(j))
tmp={}
grade=0
suject=["國文","英文","數學"]
for x in range(0,51):
    tmp[id[x]] = {}
    for u in range(0,3):
        grade =random.randint(0,100)
        tmp[id[x]][suject[u]] = grade