max = int(input())
linha = input()
linha = linha.split()

if linha[1] == "+":
    soma = int(linha[0]) + int(linha[2])
    if soma <= max:
        print('OK')
    else:
        print('OVERFLOW')
else:
    mult = int(linha[0]) * int(linha[2])
    if mult <= max:
        print('OK')
    else:
        print('OVERFLOW')
