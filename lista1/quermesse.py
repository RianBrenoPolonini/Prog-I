contador = 1
while True:
    participantes = int(input())
    if participantes == 0:
        break

    ordem = input().split()

    for i in range(participantes):
        if int(ordem[i]) == i + 1:
            print('Teste', contador)
            print(int(ordem[i]))
            print('')

    contador += 1
