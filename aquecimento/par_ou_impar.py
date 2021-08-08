contador = 1
while True:
    partidas = int(input())
    if partidas == 0:
        break
    
    j1, j2 = input(), input()
    vencedor = []

    for i in range(partidas):
        n = list(map(int, input().split()))
        if (n[0]+n[1]) % 2 == 0:
            vencedor.append(j1)
        else:
            vencedor.append(j2)

    print('Teste', contador)
    for i in range(partidas):
        print(vencedor[i])
    print()
    contador += 1
