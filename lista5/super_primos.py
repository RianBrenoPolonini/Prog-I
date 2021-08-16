import math

def primo_ou_super(n):
    if n in (0,1):
       return 'Nada'
    raiz = int(math.sqrt(n))
    for d in range(2, raiz +1):
        if n % d == 0:
            # NÃO É PRIMO
            return 'Nada'
    # É PRIMO
    n = str(n)
    cont = 0
    for x in n:
        if int(x) in (2, 3, 5, 7):
            cont += 1
    if cont == len(n):
        return 'Super'
    else:
        return 'Primo'

while True:
    try:
        n = int(input())
        print(primo_ou_super(n))
    except:
        break
