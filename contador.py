soma = maior = menor = produto = int(input('Informe o 1° numero: '))

contador = 1
while contador < 3:
    n = int(input('Informe o {}° numero: '.format(contador + 1)))
    soma = soma + n
    produto = produto * n

    if maior < n:
        maior = n
    if menor > n:
        menor = n

    contador += 1

media = soma / contador

print("""
A media é: {}
A soma é: {}
O produto é: {}
O menor é: {}
O maior é: {}
"""
      .format(media, soma, produto, menor, maior))

# print('A media é:', media)
# print('A soma é:', soma)
# print('O produto é:', produto)
# print('O menor é:', menor)
# print('O maior é:', maior)