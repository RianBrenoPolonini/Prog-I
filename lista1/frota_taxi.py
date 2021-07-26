linha = input()
linha = linha.split()

p_a = float(linha[0])
p_g = float(linha[1])
pl_a = float(linha[2])
pl_g = float(linha[3])

if p_a / pl_a < p_g / pl_g:
    print('A')
else:
    print('G')