import math
cont = 1
exp = 2
fat = 1
soma = 0
num = int(input("Digite o números de termos que deseja somar:\n"))
x = int(input("Digite um valor para x:\n "))
aux = 0
while(cont <= num):
    if(cont % 2 == 0):
        soma = soma + (x**exp/(math.factorial(fat)))
    else:
        soma = soma - (x**exp / (math.factorial(fat)))
        exp += 1
        cont += 1
    if aux == 0:
        fat += 1
        if fat == 4:
            aux += 1
    elif aux == 1:
        fat -= 1
        if fat == 1:
            aux -= 1

print('{:.3f}'.format(soma))
