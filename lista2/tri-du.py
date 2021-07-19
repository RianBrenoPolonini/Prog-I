linha = input()
cartas = list(map(int, linha.split()))

if cartas[0] >= cartas[1]:
    print(cartas[0])
else:
    print(cartas[1])