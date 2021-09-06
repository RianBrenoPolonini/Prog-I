mensagem = input()
palavra = input()
t_m = len(mensagem)
t_p = len(palavra)

def check(palavra, mensagem, i):
    for x in range(t_p):
        if palavra[x] == mensagem[i+x]:
            return False
    
    return True
    
n = 0
for i in range(t_m - t_p + 1):
    if check(palavra, mensagem, i):
        n += 1

print(n)