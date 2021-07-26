trilhas = int(input())
trilha = 1

for i in range(trilhas):
    ida = list(map(int, input().split()))
    volta =  ida[::-1]
    contador_ida = contador_volta = 0
    
    for a in range(ida.pop(0)-1):
        if ida[a] < ida[a+1]:
            contador_ida += ida[a+1] - ida[a]
        if volta[a] < volta[a+1]:
            contador_volta += volta[a+1] - volta[a]

    if i == 0:
        facil = (min(contador_volta, contador_ida))
    elif facil > (min(contador_volta, contador_ida)):
        facil = (min(contador_volta, contador_ida))
        trilha = i + 1

print(trilha)
