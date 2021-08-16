import random

def joga_dado(quantidade, face):
    dados = []
    controle = 0
    for i in range(quantidade):
        dado = random.randint(1,6)
        if dado == face:
            controle += 1
        dados.append(dado)

    return dados, (controle*100 / quantidade)
    
dados = joga_dado(50,6)
print(f'{dados[1]}%')
