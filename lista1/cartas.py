linha = input()
ordem = []
for val in linha.split():
    ordem.append(int(val))

if ordem == sorted(ordem):
    print('C')
elif ordem == sorted(ordem, reverse=True):
    print('D')
else:
    print('N')
