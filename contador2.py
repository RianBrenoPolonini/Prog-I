numeros = []
for i in range(50):
    numeros.append(int(input('Digite o numero: ')))
print(numeros)

soma, produto = 0,1

for i in range(len(numeros)):
    soma += numeros[i]
    produto *= numeros[i]

numeros.sort()
menor = numeros[0]
maior = numeros[-1]
media = soma / len(numeros)

print(f"""
A media é: {media}
A soma é: {soma}
O produto é: {produto}
O menor é: {menor}
O maior é: {maior}
""")
