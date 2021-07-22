soma = maior = menor = produto = int(input('Informe o 1° numero: '))

contador = 1
while contador < 50:
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
