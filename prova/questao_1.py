positivos = negativos = nulos = soma_positivo = soma_negativo = 0

for i in range(60):
    n = int(input(f'Digite o {i+1}° número: '))
    if n > 0:
        positivos +=1
        soma_positivo += n
    elif n < 0:
        negativos +=1
        soma_negativo += n
    else:
        nulos +=1
# Como não tem como dividir por 0, então precisos tirar essa opçao
if positivos == 0:
    media_positivo = 0  
else:
    media_positivo = soma_positivo/positivos

if negativos == 0:
    media_negativo = 0  
else:
    media_negativo = soma_negativo/negativos
      
print(f"""
Foram digitatos:
{positivos} números positivos
{negativos} números negativos
{nulos} números nulos

A média dos números positovos é: {media_positivo}
A média dos números negativos é: {media_negativo}
""")
