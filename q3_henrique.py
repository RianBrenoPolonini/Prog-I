import math

termos = int(input('Digite o número de termos: '))
x = int(input('Digite um número positivo: '))
soma, controle = 0, 1

for i in termos*(1, 2, 3, 4, 3, 2):
    if controle == termos + 1:
        break
    if controle % 2 == 0:
        soma += x ** (controle+1) / math.factorial(i)
    else:
        soma += -(x ** (controle+1) / math.factorial(i))
    controle += 1 
print(soma)
