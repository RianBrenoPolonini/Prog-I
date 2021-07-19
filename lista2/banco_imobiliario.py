linha = input()
linha = list(map(int, linha.split()))
D = E = F = linha[0]
operacoes = linha[1]

def compra(user, valor):
    global D, E, F
    if user == "D":
        D -= valor
    elif user == "E":
        E -= valor
    else:
        F -= valor

def venda(user, valor):
    global D, E, F
    if user == "D":
        D += valor
    elif user == "E":
        E += valor
    else:
        F += valor

def aluga(user, user2, valor):
    global D, E, F
    if user == "D":
        D += valor
        if user2 == "E":
            E -= valor
        else:
            F -= valor
    elif user == "E":
        E += valor
        if user2 == "D":
            D -= valor
        else:
            F -= valor
    else:
        F += valor
        if user2 == "E":
            E -= valor
        else:
            D -= valor

for i in range(operacoes):
    linha = input()
    linha = linha.split()

    if linha[0] == "C":
        compra(linha[1], int(linha[2]))
    elif linha[0] == "V":
        venda(linha[1], int(linha[2]))
    else:
        aluga(linha[1], linha[2], int(linha[3]))
    
print(D, E, F)
