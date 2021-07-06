# Desafio calculadora :)
# Biblioteca para poder limpar a tela

import os
os.system('cls') #Comando para limpar a tela

def calculadora(n1, n2, sinal):
    if (sinal == "+"):
        soma = n1 + n2
        print('A soma de', n1, 'e', n2, "é", soma, "\n")
    elif (sinal == "-"):
        subtracao = n1 - n2
        print('A subtração de', n1, 'e', n2, "é", subtracao, "\n")
    elif (sinal == "*"):
        multiplicacao = n1 * n2
        print('A multiplicação de', n1, 'e', n2, "é", multiplicacao, "\n")
    elif (sinal == "/"):
        divicao = n1 / n2
        print('A divição de', n1, 'e', n2, "é", divicao, "\n")

# Entrada de dados da calculadora
n1 = float(input('Digite o primeiro numero para calcular: '))
n2 = float(input('Digite o segundo numero para calcular: '))
sinal = str(input('Digite agora a operação (+, -, *, /): '))
os.system('cls')

calculadora(n1, n2, sinal)