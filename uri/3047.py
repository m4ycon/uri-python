m, a, b = [int(input()), int(input()), int(input())]

c = m - a - b
idades = [a, b, c]
idades.sort()

print(idades[-1])