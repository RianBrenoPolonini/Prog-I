# Desafio calculadora :)
import os
os.system('cls')

while True:
    opcao = input('Digite 1 para fazer uma conta ou 2 para sair: ')
    os.system('cls')

    if opcao == '1':
        n1 = input('Digite o primeiro numero para calcular: ')
        n2 = input('Digite o segundo numero para calcular: ')
        sinal = input('Digite agora a operação (+, -, *, /): ')
        os.system('cls')

        try:
            n1 = float(n1)
            n2 = float(n2)

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
            else:
                print(f'Operação "{sinal}" não identificada\n')

        except:
            print('Digite um número valido \n')

    elif opcao == '2':
        break
