ddd = int(input())

dddCity = [61, 'Brasilia', 71, 'Salvador', 11, 'Sao Paulo',
  21, 'Rio de Janeiro', 32, 'Juiz de Fora', 19, 'Campinas',
  27, 'Vitoria', 31, 'Belo Horizonte']

if dddCity.count(ddd) > 0:
  print(dddCity[dddCity.index(ddd) + 1])
else:
  print('DDD nao cadastrado')
