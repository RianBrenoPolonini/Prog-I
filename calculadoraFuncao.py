# Desafio calculadora :)
# Biblioteca para poder limpar a tela
import os
os.system('cls') #Comando para limpar a tela

def calculadora(n1, n2, sinal):
    if (sinal == "+"):
        result = n1 + n2
        print('A soma de {} e {} é \n'.format(n1, n2, sinal))
    elif (sinal == "-"):
        result = n1 - n2
        print('A subtração de {} e {} é \n'.format(n1, n2, sinal))
    elif (sinal == "*"):
        result = n1 * n2
        print('A multiplicação de {} e {} é \n'.format(n1, n2, sinal))
    elif (sinal == "/"):
        result = n1 / n2
        print('A soma de {} e {} é \n'.format(n1, n2, sinal))

# Entrada de dados da calculadora
n1 = float(input('Digite o primeiro numero para calcular: '))
n2 = float(input('Digite o segundo numero para calcular: '))
sinal = str(input('Digite agora a operação (+, -, *, /): '))
os.system('cls')

calculadora(n1, n2, sinal)