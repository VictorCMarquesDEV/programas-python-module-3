p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = contador = 10
while cont != 0:
    print(p, end=' -> ')
    p += r
    cont -= 1
    if cont == 0:
        print('PAUSA')
        cont = int(input('Deseja mostrar mais quantos termos? '))
        contador += cont
print('Progressão finalizada com {} termos mostrados.'.format(contador))
