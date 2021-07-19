testes = int(input())

for i in range(testes):
    alunos = int(input())
    linha = input()
    notas = list(map(int, linha.split()))
    ordem = sorted(notas, reverse=True)

    contador = 0
    for i in range(alunos):
        if notas[i] == ordem[i]:
            contador +=1
    print(contador)