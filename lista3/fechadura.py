pinos = list(map(int, input().split()))
altura = list(map(int, input().split()))
movimentos = 0 

for i in range(pinos[0]-1):
        if altura[i] < pinos[1]:
            altura[i] += pinos[1] - altura[i]
            movimentos += altura[i]
        elif altura[i] > pinos[1]:
            altura[i] += altura[i] - pinos[1]
            movimentos += altura[i]
        if altura[i+1] < pinos[1]:
            altura[i+1] += pinos[1] - (altura[i+1] + movimentos)
            movimentos += altura[i+1]
        elif altura[i+1] > pinos[1]:
            altura[i+1] += (altura[i+1] + movimentos) - pinos[1]
            movimentos += altura[i+1]
    
print(movimentos)
