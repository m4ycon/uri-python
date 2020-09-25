salary = float(input())
newSalary = salary

if 0 <= salary <= 400:
  newSalary *= 1.15
elif salary <= 800:
  newSalary *= 1.12
elif salary <= 1200:
  newSalary *= 1.1
elif salary <= 2000:
  newSalary *= 1.07
else:
  newSalary *= 1.04

print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {(newSalary - salary):.2f}')
print(f'Em percentual: {(((newSalary / salary) - 1)*100):.0f} %')