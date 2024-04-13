valores = []
menor = maior = -1

for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        menor = maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]
    if valores[c] > maior:
        maior = valores[c]

print(f'\nLista: {valores}')
print(f'Maior: {maior}')
print('Posições: ', end='')
for c in range(len(valores)):
    if valores[c] == maior:
        print(c, end='; ')

print(f'\nMenor: {menor}')
print('Posições: ', end='')
for c in range(len(valores)):
    if valores[c] == menor:
        print(c, end='; ')
