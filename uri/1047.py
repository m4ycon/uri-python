inicioH, inicioM, finalH, finalM = [int(n) for n in input().split()]

inicioM += inicioH * 60
finalM += finalH * 60

res = 0
if finalM > inicioM and 1 <= finalM - inicioM <= 24 * 60:
  res = finalM - inicioM
else:
  res = 24 * 60 + finalM - inicioM

print(f'O JOGO DUROU {res // 60} HORA(S) E {res % 60} MINUTO(S)')