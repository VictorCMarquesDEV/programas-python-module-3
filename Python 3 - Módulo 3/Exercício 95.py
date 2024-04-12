jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = int(input('Partidas: '))
    contP = 1
    soma = 0
    for c in range(0, jogador['Partidas']):
        gol = int(input(f'Gols na Partida {contP}: '))
        gols.append(gol)
        contP += 1
        soma += gol

    jogador['Gols'] = gols.copy()
    jogador['Aproveitamento'] = soma / jogador['Partidas']
    jogador['Total de Gols'] = soma
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    esc = str(input('Deseja continuar [S/N]? '))
    if esc in 'Nn':
        break

contJ = 0
print('-=-' * 16)
print('\033[7;49;32m|{:^3}|{:<20}|{:^20}|\033[m'.format('No.', 'Nome:', 'Aproveitamento: '))
for c in range(0, len(jogadores)):
    print('|{:^3}|{:<20}|{:^20.2f}|'.format(contJ, jogadores[c]['Nome'], jogadores[c]['Aproveitamento']))
    contJ += 1

print('-=-' * 30)
while True:
    cont = 1
    esc2 = int(input('Mostrar detalhamento de qual jogador [Negativo interrompe]? '))
    if esc2 < 0:
        break
    print('\033[7;49;32m|{:^3}|{:<20}|{:^20}|{:^20}|{:^20}|\033[m'.format('No.', 'Nome:', 'Partidas',
                                                                          'Aproveitamento', 'Total de Gols'))
    print('|{:^3}|{:<20}|{:^20}|'.format(esc2, jogadores[esc2]['Nome'], jogadores[esc2]['Partidas']), end='')
    print('{:^20.2f}|'.format(jogadores[esc2]['Aproveitamento']), end='')
    print('{:^20}|'.format(jogadores[esc2]['Total de Gols']))
    for c in jogadores[esc2]['Gols']:
        print(f'   > Na partida {cont}, fez {c} gol(s)')
        cont += 1
    print('-=-' * 30)
print('PROGRAMA ENCERRADO!')
