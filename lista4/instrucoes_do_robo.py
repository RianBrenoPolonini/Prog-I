for i in range(int(input())):
    intrucoes = []
    for i in range(int(input())):
        comando = input()

        if comando == 'LEFT':
            intrucoes.append(-1)
        elif comando == 'RIGHT':
            intrucoes.append(1)
        else:
            comando = comando.split()
            intrucoes.append(intrucoes[int(comando[2])-1])

    print(sum(intrucoes))