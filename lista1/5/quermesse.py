# Contador para printar o numero do teste
contador = 1
while True:
    participantes = int(input())
    # Verifica se tem 0 participantes, se for o caso para o lool
    if participantes == 0:
        break

    linha = input()
    ordem = linha.split()  # Transforma em lista

    for i in range(participantes):
        if int(ordem[i]) == i + 1:
            print('Teste', contador)
            print(int(ordem[i]))
            print('')

    contador += 1
