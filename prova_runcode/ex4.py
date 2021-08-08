n_a = int(input())
n_b = int(input())
n_c = int(input())

valor = []
valor.append(n_b * 2 + n_c * 4)
valor.append(n_a * 2 + n_c * 2)
valor.append(n_a * 4 + n_b * 2)

print(min(valor))
