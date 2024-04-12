c = 1
while c < 11:
    print(c)
    c += 1

contpar = contimpar = 0
n = -1
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        contpar += 1
    else:
        contimpar += 1
print('Pares: {}\nÍmpares: {}'.format(contpar - 1, contimpar))
