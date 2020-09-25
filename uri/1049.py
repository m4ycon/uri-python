escolha = input()

res = ''
if escolha == 'vertebrado':
  escolha = input()
  if escolha == 'ave':
    escolha = input()
    if escolha == 'carnivoro':
      res = 'aguia'
    else:
      res = 'pomba'
  else:
    escolha = input()
    if escolha == 'onivoro':
      res = 'homem'
    else:
      res = 'vaca'
else:
  escolha = input()
  if escolha == 'inseto':
    escolha = input()
    if escolha == 'hematofago':
      res = 'pulga'
    else:
      res = 'lagarta'
  else:
    escolha = input()
    if escolha == 'hematofago':
      res = 'sanguessuga'
    else:
      res = 'minhoca'

print(res)