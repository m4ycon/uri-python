while True:
  try:
    num = int(input())
    res = 1
    resLength = 1
    while res % num != 0:
      resLength += 1
      res = int('1' * resLength)
    print(resLength)
  except EOFError:
    break
