lista = list()
par = list()
impar = list()
for c in range(0, 7):
    a = int(input(f'Digite o {c + 1}° número: '))
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])
print(f'\n{lista}')
print(f'Pares: {lista[0]}')
print(f'Ímpares: {lista[1]}')
