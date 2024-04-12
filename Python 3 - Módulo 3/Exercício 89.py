pessoas = []
dados = []
cont = 0

while True:
    print('-=-' * 10)
    print(f'Aluno {cont + 1}')
    print('-=-' * 10)
    dados.append(cont)
    dados.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    dados.append(n1)
    n2 = float(input('Nota 2: '))
    dados.append(n2)
    media = (n1 + n2) / 2
    dados.append(media)
    pessoas.append(dados[:])
    dados.clear()
    cont += 1

    esc = str(input('Deseja continuar [S/N]? '))
    if esc in 'Nn':
        break

print('-=-' * 16)
print('\033[7;49;32m|{:^3}|{:^10}|{:^10}|\033[m'.format('N°.', 'Nome', 'Média'))
for c in range(0, len(pessoas)):
    print('|{:^3}'.format(pessoas[c][0]), end='')
    print('|{:<10}'.format(pessoas[c][1]), end='')
    print('|{:^10.2f}|'.format(pessoas[c][4]), end='')
    print('')
print('-=-' * 16)

while True:
    esc2 = int(input('Mostrar notas de qual aluno [Negativo interrompe]? '))
    if esc2 < 0:
        break
    print('\033[7;49;32m|{:^3}|{:^10}|{:^10}|{:^10}|{:^10}|\033[m'.format('N°.', 'Nome', 'Nota 1', 'Nota 2', 'Média'))
    for p in range(0, 5):
        print('|', end='')
        if p == 0:
            print('{:^3}'.format(pessoas[esc2][p]), end='')
        elif p == 1:
            print('{:<10}'.format(pessoas[esc2][p]), end='')
        else:
            print('{:^10.2f}'.format(pessoas[esc2][p]), end='')
        if p == 4:
            print('|', end='')
    print('')
    print('-=-' * 16)
