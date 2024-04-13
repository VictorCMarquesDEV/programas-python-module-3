jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input('Partidas: '))
cont = 1
soma = 0

for c in range(0, jogador['Partidas']):
    gol = int(input(f'Gols na Partida {cont}: '))
    gols.append(gol)
    cont += 1
    soma += gol

jogador['Gols'] = gols.copy()
jogador['Aproveitamento'] = soma/jogador['Partidas']
jogador['Total de Gols'] = soma

print('-=-' * 10)
for k, v in jogador.items():
    print(f'{k}: {v}')
cont = 1
for c in gols:
    print(f'   > Na partida {cont}, fez {c} gols')
    cont += 1
