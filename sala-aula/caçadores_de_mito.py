raios = int(input())
controle = []

for i in range(raios):
    n = input()
    controle.append(n)

if len(controle) == len(set(controle)):
    print(0)
else:
    print(1)
