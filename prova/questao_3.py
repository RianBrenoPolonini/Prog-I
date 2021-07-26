import math

parcelas = int(input('Digite o número de termos: '))
x = int(input('Digite um número positivo: '))
soma = 0

for i in range(1, parcelas + 1):
    if i % 6 == 1 % 6:
        n = math.factorial(1)
    elif i % 6 == 2 % 6:
        n = math.factorial(2)
    elif i % 6 == 3 % 6:
        n = math.factorial(3)
    elif i % 6 == 4 % 6:
        n = math.factorial(4)
    elif i % 6 == 5 % 6:
        n = math.factorial(3)
    else:    
        n = math.factorial(2)

    if i % 2 == 0:
        soma += x ** (i+1) / n
    else:
        soma += -(x ** (i+1) / n)
print(soma)
