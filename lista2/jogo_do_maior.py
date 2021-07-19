while True:

    rodadas = int(input())
    if rodadas == 0:
        break

    jogador1 = jogador2 = 0
    for i in range(rodadas):
        linha = input()
        n = list(map(int, linha.split()))
        
        if n[0] > n[1]:
            jogador1 +=1
        elif n[0] < n[1]:
            jogador2 +=1
    
    print(jogador1, jogador2)
