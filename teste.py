# Este programa tem como função ser uma calculadora de operações básicas.

# Condição para que o programa entre em um loop.
while True:
    print('Tipos de operadores da calculadora:\nsoma => +\nsubtração => -\nmultiplicação => *\ndivisão => /')

    # Entrada de dados.
    operador = input('Digite um dos operadores acima: ')
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))

    # Condição para ser feita cada operação com suas respectivas saídas.
    if operador == '+':
        calculo = num1 + num2
        print('{} + {} = {}'.format(num1, num2, calculo))
    elif operador == '-':
        calculo = num1 - num2
        print('{} - {}  = {}'.format(num1, num2, calculo))
    elif operador == '*':
        calculo = num1 * num2
        print('{} * {} = {}'.format(num1, num2, calculo))
    elif operador == '/':
        calculo = num1 / num2
        print('{} / {} = {}'.format(num1, num2, calculo))