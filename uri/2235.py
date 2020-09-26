t1, t2, t3 = [int(n) for n in input().split()]

if t1 + t2 == t3 or t1 + t3 == t2 or t2 + t3 == t1 or t1 == t2 or t1 == t3 or t2 == t3:
  print('S')
else:
  print('N')