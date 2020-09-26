laugh = str(input())

really_fun = ''
for l in laugh:
  if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    really_fun += l

if really_fun == really_fun[::-1]:
  print('S')
else:
  print('N')
