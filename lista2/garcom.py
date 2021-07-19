bandejas = int(input())
contador = 0

for i in range(bandejas):
    linha = input()
    n = list(map(int, linha.split()))
    if n[0] > n[1]:
        contador += n[1]

print(contador)