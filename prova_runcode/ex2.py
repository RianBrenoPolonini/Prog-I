contador = 1
while True:
    n = int(input())
    if n == -1:
        break
    
    base, mult = 2, 1

    for i in range(n):
        base += mult
        mult *= 2

    print('Teste', contador)
    print(base**2)
    print()

    contador += 1
