for i in range(int(input())):
    linha = input().split()

    if linha[0][len(linha[0]) - len(linha[1]):] == linha[1]:
        print('encaixa')
    else:
        print('nao encaixa')
