linha = input()
linha = linha.split()

xm = int(linha[0])
ym = int(linha[1])
xr = int(linha[2])
yr = int(linha[3])

print(abs((xm - xr)) + abs((ym - yr)))