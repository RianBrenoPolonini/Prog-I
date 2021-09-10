risada = input()
vogais = []

for i in risada:
  if i in ('a', 'e', 'i', 'o', 'u'):
      vogais.append(i)

if vogais == vogais[::-1]:
  print('S')
else:
  print('N')
