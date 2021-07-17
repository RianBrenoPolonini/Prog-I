linha = int(input())
coluna = int(input())

linha_final = 0
coluna_final = 0

if linha % 2 != 0:
    linha_final = 1

if linha_final == 1 and coluna % 2 != 0:
    print(1)
elif linha_final == 0 and coluna % 2 == 0:
    print(1)
else:
    print(0)
