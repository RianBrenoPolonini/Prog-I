import math

parcelas = int(input('Digite o número de termos: '))
x = int(input('Digite um número positivo: '))
soma, expoente = 0, 2

def fatorial(i):
    if i % 6 == 2 % 6:
        n = math.factorial(2)
    elif i % 6 == 3 % 6:
        n = math.factorial(3)
    elif i % 6 == 4 % 6:
        n = math.factorial(4)
    elif i % 6 == 5 % 6:
        n = math.factorial(3)
    elif i % 6 == 6 % 6:
        n = math.factorial(2)
    else:    
        n = math.factorial(1)
    return n

for i in range(1, parcelas + 1):
    if i % 2 == 0:
        soma += x ** expoente / fatorial(i)
    else:
        soma -= x ** expoente / fatorial(i)
    expoente +=1
print(soma)
