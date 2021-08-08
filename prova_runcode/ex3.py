linha = list(map(int,input().split()))

if ((linha[0] - linha[1] + linha[2] == 0) or (linha[0] + linha[1] - linha[2] == 0)):
    print('S')
elif ((linha[2] - linha[0] + linha[1] == 0) or (linha[2] + linha[1] - linha[0] == 0)):
    print('S')
elif ((linha[0] - linha[1] == 0) or (linha[0] - linha[2] == 0) or (linha[1] - linha[2] == 0)):
    print('S')
else:
    print('N')
