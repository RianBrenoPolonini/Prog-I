linha = list(map(float, input().split()))

if linha[0] / linha[2] < linha[1] / linha[3]:
    print('A')
else:
    print('G')