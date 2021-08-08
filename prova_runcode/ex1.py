linha = list(map(int,input().split()))
nsorte = list(map(int,input().split()))
pontuacao = []
ganhador = contador = 0

for i in range(linha[1]):
    for x in range(linha[0]):
        if contador == 0:
            pontuacao.append(nsorte[x+contador*linha[0]])
        else:
            pontuacao[x] += nsorte[x+contador*linha[0]]
    contador +=1
    
maior = pontuacao[0]
for i in range(linha[0]):
    if pontuacao[i] >= maior:
        maior = pontuacao[i]
        ganhador = i+1

print(ganhador)
