# Desafio calculadora :)
# Biblioteca para poder limpar a tela
import os
os.system('cls') #Comando para limpar a tela

# Loop infinito
while 1==1:
    # Opcão para o usuario continuar ou parar
    opcao = int(input('Digite 1 para fazer uma conta ou 2 para sair: '))
    os.system('cls')

    if opcao == 1:
        # Entrada de dados da calculadora
        primeiroNumero = float(input('Digite o primeiro numero para calcular: '))
        segundoNumero = float(input('Digite o segundo numero para calcular: '))
        operacao = str(input('Digite agora a operação (+, -, *, /): '))
        os.system('cls')
        
        if (operacao == "+"):
            soma = primeiroNumero + segundoNumero
            print('A soma de', primeiroNumero, 'e', segundoNumero, "é", soma, "\n")
        elif (operacao == "-"):
            subtracao = primeiroNumero - segundoNumero
            print('A subtração de', primeiroNumero, 'e', segundoNumero, "é", subtracao, "\n")
        elif (operacao == "*"):
            multiplicacao = primeiroNumero * segundoNumero
            print('A multiplicação de', primeiroNumero, 'e', segundoNumero, "é", multiplicacao, "\n")
        elif (operacao == "/"):
            divicao = primeiroNumero / segundoNumero
            print('A divição de', primeiroNumero, 'e', segundoNumero, "é", divicao, "\n")
            
    # Sair do loop
    elif opcao == 2:
        break # Comando para parar o while