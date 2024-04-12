def contador(inicio, final, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio:  início da contagem
    :param final: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    Função criada por VCM
    """
    for i in range(inicio, final + 1, passo):
        print(i, end=' ')
    print('FIM!')


help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)


somar(1, 2)
