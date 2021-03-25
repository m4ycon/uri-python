def bag(bag_max_weight, values_and_weights):
  n_lines = len(values_and_weights)+1
  n_columns = bag_max_weight+1

  matrix, matrix_items_used = [], []
  for i in range(n_lines):
    matrix.append([0]*n_columns)
    matrix_items_used.append([0]*n_columns)
    for j in range(n_columns):
      matrix_items_used[i][j] = []

  weights = [0] + [item[1] for item in values_and_weights]
  values = [0] + [item[0] for item in values_and_weights]

  for i in range(1, n_lines): # i do item atual que pode ou n ser inserido
    for j in range(1, n_columns): # j do peso maximo da mochila
      if weights[i] > j: # quando o item não cabe
        matrix[i][j] = matrix[i-1][j]
        matrix_items_used[i][j] = matrix_items_used[i-1][j]
      else: # testa qual o melhor, colocar o item ou não
        usa = values[i] + matrix[i-1][j-weights[i]]
        nao_usa = matrix[i-1][j]
        matrix[i][j] = max([usa, nao_usa])

        matrix_items_used[i][j] = matrix_items_used[i-1][j] if nao_usa > usa else matrix_items_used[i-1][j-weights[i]] + [i-1]

  return matrix[-1][-1], matrix_items_used[-1][-1]



# [[valor, peso], ...]
valor_e_peso = [[60,1],[150,3],[120,3],[160,4],[200,5],[150,5],[60,6]]
peso_max_mochila = 6

# retorna a melhor combinação de itens que cabem na mochila e com o maior valor possível
maior_lucro, itens_usados = bag(peso_max_mochila, valor_e_peso)

print(maior_lucro) # 270
print(itens_usados) # [1, 2]
