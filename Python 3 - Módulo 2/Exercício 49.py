n = int(input('Digite um número: '))
print('\nTabuada do {}:'.format(n))
for c in range(1, 11):
    print('{} * {:2} = {}'.format(n, c, n * c))
