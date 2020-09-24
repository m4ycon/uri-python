nAmigos, nMusicas, musicaAtual = [int(i) for i in input().split()]
trocas = 0
adoraDetesta = []
for n in range(nAmigos):
  # [adora, detesta]
  adoraDetesta.append([int(i) for i in input().split()])

alguemDetesta = [0]*nAmigos
for i1, amigo1 in enumerate(adoraDetesta):
  for i2, amigo2 in enumerate(adoraDetesta):
    if amigo1[1] == amigo2[0] and i1 != i2:
      alguemDetesta[i2] = 1

while True and alguemDetesta.count(0) > 0:
  musicaAntiga = musicaAtual
  for index, amigo in enumerate(adoraDetesta):
    if amigo[1] == musicaAtual:
      indexMaisVelho = index
      for i in range(index - 1, -1, -1):
        if adoraDetesta[i][1] == musicaAtual:
          indexMaisVelho = i
      musicaAtual = adoraDetesta[indexMaisVelho][0]
      trocas += 1

  if musicaAntiga == musicaAtual:
    break

if alguemDetesta.count(0) > 0:
  print(trocas)
else:
  print(-1)