import math

num_termos = int(input('Informe o número de termos: '))
x = int(input('Informe o valor de X: '))
soma, ex = 0, 1

while ex != (num_termos + 1):
    for divisor in (1, 2, 3, 4, 3, 2):
        if ex == (num_termos + 1):
            break
        ex += 1
        if divisor % 2 == 0:
            soma += x ** ex / math.factorial(divisor)
        else:
            soma -= x ** ex / math.factorial(divisor)

print(soma)
