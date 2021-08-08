contador, ganhador = 1, 0

while True:
    rodadas = list(map(int, input().split()))
    if rodadas[0] == 0:
        break

    fila = list(map(int, input().split()))

    for i in range(rodadas[1]):
        n = list(map(int, input().split()))
        for ind in range(2,n):
            if n[1] != n[i]:
                del(fila[ind-2])
    print(fila)
