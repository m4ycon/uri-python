renda = float(input())

res = 0
if renda <= 2000:
  print('Isento')
else:
  if renda <= 3000:
    res += (renda - 2000) * 0.08
  elif renda <= 4500:
    res += 1000 * 0.08 + (renda - 3000) * 0.18
  else:
    res += 1000 * 0.08 + 1500 * 0.18 + (renda - 4500) * 0.28

  print(f'R$ {res:.2f}')