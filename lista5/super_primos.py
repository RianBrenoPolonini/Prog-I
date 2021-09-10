import math

def primo_ou_super(n):
    if n in (0,1):
       return 'Nada'
    for d in range(2, int(math.sqrt(n)) +1):
        if n % d == 0:
            return 'Nada'
    for x in str(n):
        if int(x) not in (2, 3, 5, 7):
            return 'Primo'
    return 'Super'
        
while True:
    try:
        n = int(input())
        print(primo_ou_super(n))
    except:
        break
