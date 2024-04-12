def aumentar(valor, porcent, show=True):
    v = valor + (valor * porcent / 100)
    if show:
        return fmt(v)
    else:
        return v


def diminuir(valor, porcent, show=True):
    v = valor - (valor * porcent / 100)
    if show:
        return fmt(v)
    else:
        return v


def dobro(valor, show=True):
    if show:
        return fmt(valor * 2)
    else:
        return valor * 2


def metade(valor, show=True):
    if show:
        return fmt(valor / 2)
    else:
        return valor / 2


def fmt(valor):
    texto = f'R${valor:.2f}'
    texto = texto.replace('.', ',')
    return texto


def resumo(valor, a, r):
    print('=' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('=' * 30)
    print(f'Preço analisado: {fmt(valor)}')
    print(f'Dobro do preço: {dobro(valor, True)}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'{a}% de aumento: {aumentar(valor, a, True)}')
    print(f'{r}% de redução {diminuir(valor, r, True)}')
    print('=' * 30)
