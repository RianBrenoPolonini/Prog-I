lista = list(map(int, input().split()))
resultado = -1

if(lista[0]!=lista[1] and lista[2]!=lista[3]):
    fim = lista[2]
    inicio = lista[0]
    while(inicio<=fim):
        if(inicio%lista[0]==0 and inicio%lista[1]!=0 and lista[2]%inicio==0 and lista[3]%inicio!=0):
            resultado = inicio
            break
        inicio += lista[0]

print(resultado)
