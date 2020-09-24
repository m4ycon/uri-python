while True:
  nValues = int(input())
  if nValues == 0:
    break

  values = []
  for n in range(nValues):
    num = float(input())
    values.append(num)

  average = round(sum(values)/len(values), 2)

  payback = 0
  for value in values:
    if value < average:
      payback += average - value

  print('${:.2f}'.format(payback))
