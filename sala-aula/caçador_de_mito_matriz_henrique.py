raios = int(input())
matriz = []

for _ in range(501):
    matriz.append([0]*501)

controle = False
for x in range(raios):
    coord = list(map(int, input().split()))
    if matriz[coord[0]][coord[1]] == 0:
        matriz[coord[0]][coord[1]] = 1
    else:
      controle = True
      break 

if controle == False:
    print(0)
else:
    print(1)