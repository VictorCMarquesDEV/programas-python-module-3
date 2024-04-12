esc = -1
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
while esc != 5:
    print('\nO que deseja?')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do programa')
    esc = int(input('=> '))
    if esc == 1:
        print('\nSoma:\n{:.2f} + {:.2f} = {:.2f}'.format(n1, n2, n1 + n2))
    elif esc == 2:
        print('\nMultiplicação\n{:.2f} * {:.2f} = {:.2f}'.format(n1, n2, n1 * n2))
    elif esc == 3:
        if n1 > n2:
            print('\n{:.2f} é maior que {:.2f}'.format(n1, n2))
        elif n2 > n1:
            print('\n{:.2f} é maior que {:.2f}'.format(n2, n1))
        else:
            print('\n{:.2f} e {:.2f} são iguais'.format(n1, n2))
    elif esc == 4:
        n1 = float(input('\nDigite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif esc < 1 or esc > 5:
        print('\nOpção errada. Tente novamente!')
