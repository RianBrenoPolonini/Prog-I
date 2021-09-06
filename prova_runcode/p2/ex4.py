import sys

def cont_dias(dias, chocadeiras, frangos, maior):
    contador = 1
    while contador < maior:
        medio = (contador + maior) >> 1
        itm = busca(dias, chocadeiras, medio)
 
        if itm < frangos:
            contador = medio + 1
        else:
            maior = medio
    return maior

def busca(dias, chocadeiras, tempo):
    contador = 0
    for i in range(chocadeiras):
        contador += tempo // dias[i]
    return contador

def pega_maior(dias, chocadeiras, frangos):
    maior = -sys.maxsize
    for i in range(chocadeiras):
        maior = max(maior, dias[i])

    return cont_dias(dias, chocadeiras, frangos, maior * frangos)
 
chocadeiras, frangos = map(int, input().split())
dias = list(map(int, input().split()))

print(pega_maior(dias, chocadeiras, frangos))

""""
3 20
2 3 5
20

4 43
2 3 4 5
35
"""