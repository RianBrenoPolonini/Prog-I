pacotes = int(input())
pesos = list(map(int, input().split()))
pesos.sort()

def check_possivel():
    if pesos[0] > 8:
        return 'N'
    for i in range(pacotes-1):
        if (pesos[i+1] - pesos[i]) > 8:
            return 'N'
    return 'S' 

print(check_possivel())
