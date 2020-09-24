cod, quant = [int(n) for n in input().split()]

products = [4, 4.5, 5, 2, 1.5]
price = products[cod - 1] * quant

print(f'Total: R$ {price:.2f}')