def combinations(arr, aux_arr = [], n_atual = 0):
  if len(arr) == n_atual:
    return

  for n in arr[n_atual:]:
    aux_arr.append(n)
    n_atual += 1
    print(aux_arr)
    combinations(arr, aux_arr, n_atual)
    aux_arr.pop()
    
combinations([1, 2, 3, 4, 5, 6, 7])
