premiados = int(input())
tamSolic = [int(i) for i in input().split()]
peqSolic, medSolic = [tamSolic.count(1), tamSolic.count(2)]
peqProd, medProd = [int(input()), int(input())]

if peqProd >= peqSolic and medProd >= medSolic:
  print('S')
else:
  print('N')