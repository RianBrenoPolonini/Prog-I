q = int(input())
for i in range(q):
    m = int(input())
    n = int(input())
    soma = 0
   
    contador = 1
    while contador <= n:
        if m % 2 == 0:
            soma +=m
            m +=1
            contador +=1
        else:
            m +=1

    print(soma)
