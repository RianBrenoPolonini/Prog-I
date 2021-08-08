for i in range(int(input())):
    linha = input().split()
    n1 = linha[0]

    if n1[len(n1) - len(linha[1]):] == linha[1]:
        print('encaixa')
    else:
        print('nao encaixa')
