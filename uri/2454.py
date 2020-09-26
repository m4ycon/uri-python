p, r = [int(n) for n in input().split()]

res = p + r
if res <= 1 and p != 1:
  print('C')
elif res == 2:
  print('A')
else:
  print('B')