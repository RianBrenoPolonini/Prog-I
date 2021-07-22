trilhas = int(input())

for i in range(trilhas):
    ida = list(map(int, input().split()))
    volta =  ida[::-1]
    contador_ida = contador_volta = 0
    facil = []

    for i in range(ida.pop(0)-1):
        if ida[i] < ida[i+1]:
            contador_ida += ida[i+1] - ida[i]
        if volta[i] < volta[i+1]:
            contador_volta += volta[i+1] - volta[i]

    facil.append(min(contador_volta, contador_ida)) 

print(min(facil))