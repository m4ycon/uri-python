pInp = str(input())
aInp = str(input())

p, a = [[], []]
for l in pInp:
  p.append(l)

for l in aInp:
  a.append(l)

i = 0
while i < len(p):
  for j in range(i, len(p)):
    print()
