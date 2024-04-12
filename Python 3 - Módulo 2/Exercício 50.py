soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Forneça o {}° número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('\nNúmeros Contados: {}\nSoma = {}'.format(cont, soma))
