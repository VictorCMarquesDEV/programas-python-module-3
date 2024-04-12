p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 10
while cont != 0:
    print(p, end=' -> ')
    p += r
    cont -= 1
print('FIM')
