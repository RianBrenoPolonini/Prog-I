contador = produto = 1
soma = maior = menor = 0

while contador != 4:
    print('Informe o', contador, '° numero')
    n = int(input())
    soma = soma + n
    produto = produto * n

    if contador == 1:
        menor = n
        maior = n
        
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    contador = contador + 1

media = soma / (contador - 1)
print('A media é:', media)
print('A soma é:', soma)
print('O produto é:', produto)
print('O menor é:', menor)
print('O maior é:', maior)