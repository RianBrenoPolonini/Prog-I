def primeiras_letras(frase):
    frase = frase.split()
    palavra = ''

    for i in range(len(frase)):
        palavra += frase[i][0]
        
    return palavra


# Dessa forma ele ler uma frase e já printa as primeiras letras dela
print(primeiras_letras(input()))
