
n = int(input('輸入整數n:'))
x = n // 2
for i in range(-x,x+1):
  y = abs(i)
  print(' '*y + '*'*(n-y*2) + ' '*y)