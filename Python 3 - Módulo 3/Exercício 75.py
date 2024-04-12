numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print(f'\nVocê digitou os valores {numeros}')
print(f'O 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O 3 não foi digitado')
print('Valores pares: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
