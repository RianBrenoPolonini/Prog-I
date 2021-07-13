# Entrada dos dados
peso = float(input('Qual seu peso (KG): '))
altura = float(input('Qual sua altura (m): '))
# Calcula o imc
imc = peso / (altura ** 2)

if (imc < 18.5):
    print('Abaixo do peso')
elif (imc >= 18.5 and imc < 25.5):
    print('Saudável')
elif (imc >= 25.5 and imc < 30):
    print('Peso em excesso')
elif (imc >= 30 and imc < 35):
    print('Obesidade grau I')
elif (imc >= 35 and imc < 40):
    print('Obesidade grau II')
elif (imc >= 40):
    print('Obesidade grau III')