# Desafio calculadora :)
import os

while True:
    opcao = int(input('Digite 1 para fazer uma conta ou 2 para sair: '))
    os.system('cls')
    
    if opcao == 1:
        n1 = float(input('Digite o primeiro numero para calcular: '))
        n2 = float(input('Digite o segundo numero para calcular: '))
        sinal = input('Digite agora a operação (+, -, *, /): ')
        os.system('cls')
        
        if (sinal == "+"):
            result = n1 + n2
            print(f'A soma de {n1} e {n2} é {result}\n')
        elif (sinal == "-"):
            result = n1 - n2
            print(f'A subtração de {n1} e {n2} é {result}\n')
        elif (sinal == "*"):
            result = n1 * n2
            print(f'A multiplicação de {n1} e {n2} é {result}\n')
        elif (sinal == "/"):
            result = n1 / n2
            print(f'A divição de {n1} e {n2} é {result}\n')
            
    elif opcao == 2:
        break 
