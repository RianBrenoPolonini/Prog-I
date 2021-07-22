lote = 100
mm = maior = menor = tarde = manha = 0 
for i in range(lote):
    nome = input('Digite o nome do torneiro mecânico: ')
    codigo = input('Digite o código da usada na fabricação: ')
    d1 = float(input('Digite o valor da 1° dimensão: '))
    d2 = float(input('Digite o valor da 2° dimensão: '))
    d3 = float(input('Digite o valor da 3° dimensão: '))
    data = input('Digite a data de fabricação: ')
    periodo = int(input('Digite 1 se foi fabricado de manhã ou 2 se foi a tarde: '))
    media = (d1 + d2 + d3) /3
    mm += media

    if media <= 11.48:
        situacao = "Rejeitada"
    elif media <= 11.51:
        situacao = "Aprovada"
    else:
        situacao = "Reaproveitada"

    if i == 0:
        menor = media
        maior = media   
    if maior < media:
        maior = media
    if menor > media:
        menor = media
    if periodo == 1:
        manha +=1
    if periodo == 2:
        tarde +=1

    print(f"""
    {nome}
    A média das dimensões: {media}
    Situação: {situacao}""")

mm /= lote
print(f"""
A média das média é: {mm}
A menor média é: {menor}
A maior média é: {maior}
Foram fabricadas:
{manha} peças no período da manhâ
{tarde} peças no período da tarde""")
