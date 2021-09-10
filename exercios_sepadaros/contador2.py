n = []
soma, produto, ind = 0, 1, 5

for i in range(ind):
    n.append(int(input(f'Digite o {i + 1}° número: ')))
    soma += n[i]
    produto *= n[i]

print(f"""
A media é: {soma / ind}
A soma é: {soma}
O produto é: {produto}
O menor é: {min(n)}
O maior é: {max(n)}
""")
