frase = str(input('Digite uma frase: ')).lower().split()
normal = ''.join(frase)
inverso = ''
for c in range(len(normal) - 1, -1, -1):
    inverso += normal[c]
if normal == inverso:
    print('PALÍNDROMO')
else:
    print('NÃO É PALINDROMO')

# inverso = normal[::-1]
