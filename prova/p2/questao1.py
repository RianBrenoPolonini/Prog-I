def leia_numeros():
    arq = open('numeros.txt')

    pares = []
    impares = []

    for linha in arq:
        if int(linha) % 2 == 0:
            pares.append(int(linha))
        else:
            impares.append(int(linha))

    arq.close()

    return pares, impares

def pares_impares(n):
    arq = open('pares.txt', 'w')

    for i in n[0]:
        arq.write(str(i))
        arq.write('\n')

    arq.close()

    arq = open('impares.txt', 'w')

    for i in n[1]:
        arq.write(str(i))
        arq.write('\n')

    arq.close()

pares_impares(leia_numeros())

