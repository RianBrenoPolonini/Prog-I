soma = maior = menor = produto = int(input('Informe o 1° numero: '))

contador = 1
while contador < 3:
    n = float(input(f'Informe o {contador + 1}° numero: '))
    soma = soma + n
    produto = produto * n

    if maior < n:
        maior = n
    if menor > n:
        menor = n

    contador += 1

media = soma / contador

print(f"""
A media é: {media}
A soma é: {soma}
O produto é: {produto}
O menor é: {menor}
O maior é: {maior}
""")

# print("""
# A media é: {}
# A soma é: {}
# O produto é: {}
# O menor é: {}
# O maior é: {}
# """
#       .format(media, soma, produto, menor, maior))

# print('A media é:', media)
# print('A soma é:', soma)
# print('O produto é:', produto)
# print('O menor é:', menor)
# print('O maior é:', maior)
