valores = []
esc = []
par = []
impar = []

while True:
    valores.append(int(input(f'Digite um número: ')))
    while esc != 'S' and esc != 'N':
        esc = str(input('Deseja continuar [S/N]? ')).upper()
    if esc == 'N':
        break
    esc = []

for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        par.append(valores[c])
    else:
        impar.append(valores[c])

print(f'Lista: {valores}')
print(f'Lista Par: {par}')
print(f'Lista Impar: {impar}')
