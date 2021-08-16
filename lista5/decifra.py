cript = input()
frase = input()

alfa = 'abcdefghijklmnopqrstuvwxyz'
frase_desc = ''

for i in frase:
    frase_desc += alfa[cript.index(i)]

print(frase_desc)