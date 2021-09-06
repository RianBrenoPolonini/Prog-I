n = int(input())

for i in range(n):
    frase = input().split()
    senha = ''
    
    for i in range(len(frase)):
        senha += frase[i][0]
        
    print(senha)