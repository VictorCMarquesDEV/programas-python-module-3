maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        menor = maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('\nMaior peso: {:.2f} Kg\nMenor peso: {:.2f} Kg'.format(maior, menor))
