postos, dist_inter = map(int, input().split())
n = list(map(int, input().split()))
contador = 1

for i in range(postos-1):
    if n[i+1] - n[i] <= dist_inter:
        contador += 1

if contador == postos and n[-1] + dist_inter >= 42195:
    print('S')
else:
    print('N')
