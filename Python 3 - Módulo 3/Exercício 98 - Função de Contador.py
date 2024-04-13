from time import sleep


def contador(inicio, fim, passo):
    linha()
    if passo == 0:
        passo = 1
    else:
        passo = passo.__abs__()
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')
    sleep(1)
    if fim < inicio:
        fim -= 1
        passo *= -1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!')
    sleep(2)


def linha():
    print('=' * 40)


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personlizar a contagem!')
contador(int(input('Início: ')), int(input('Fim:    ')), int(input('Passo:  ')))
