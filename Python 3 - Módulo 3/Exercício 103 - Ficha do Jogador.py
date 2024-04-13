def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = str(input('Nome: ')).strip()
g = str(input('Gols: ')).strip()
if g.isnumeric():
    print(ficha(n, g))
else:
    print(ficha(n, 0))
