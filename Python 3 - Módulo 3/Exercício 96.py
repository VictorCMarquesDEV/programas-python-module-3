def cabecalho(msg):
    print('=' * 40)
    print('{:^40}'.format(msg))
    print('=' * 40)


def area(larg, comp):
    a = larg * comp
    print(f'Área = {a:.2f}m²')


cabecalho('Controle de Terrenos')
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
