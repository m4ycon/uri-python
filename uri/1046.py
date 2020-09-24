inicio, final = [int(n) for n in input().split()]

res = 0
if final > inicio and not (-1 <= final - inicio <= 1):
  res = abs(final - inicio)
else:
  res = abs(24 + final - inicio)

print(f'O JOGO DUROU {res} HORA(S)')