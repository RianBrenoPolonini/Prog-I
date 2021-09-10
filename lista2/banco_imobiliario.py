linha = list(map(int, input().split()))
D = E = F = linha[0]

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

for i in range(linha[1]):
    operacoes = input().split()

    if operacoes[0] == "C":
        compra(operacoes[1], int(operacoes[2]))
    elif operacoes[0] == "V":
        venda(operacoes[1], int(operacoes[2]))
    else:
        aluga(operacoes[1], operacoes[2], int(operacoes[3]))
    
print(D, E, F)
