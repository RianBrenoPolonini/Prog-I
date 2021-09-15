def fibonacci(n):
    fibonacci = [1]*n

    t1 = 0
    t2 = 1

    for i in range(1,n):
        fibonacci[i] = t1 + t2
        t1 = t2
        t2 = fibonacci[i]
        
    return fibonacci

def pertencem(lista, fibonacci):
    for i in lista:
        if i not in fibonacci:
            return "Não pertencem a sequencia Fibonacci!"

    return "Pertencem a sequencia Fibonacci!"


# A questão não foi muito clara se todos os item do vetor precisam pertencer a sequencia ou se individualmente, então fiz se todos os item pertecerem

# Lista com números que tem na sequencia Fibonacci
lista_pertence = [1, 21, 1983924214061919432247806074196061, 173402521172797813159685037284371942044301]

# Lista com números que não tem na sequencia Fibonacci
lista_nao_pertence = [4, 62, 3788906237314894, 1071686518197123268779268954655565665]

print(pertencem(lista_pertence,fibonacci(200)))

print(pertencem(lista_nao_pertence,fibonacci(200)))

