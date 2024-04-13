from random import randint
num = dict()
cont = 1
for c in range(0, 4):
    j = str(input(f'Jogue o dado Jogador {c + 1} [Jogar]: ')).upper()
    while j != 'JOGAR':
        j = str(input(f'Jogue o dado Jogador {c + 1} [Jogar]: ')).upper()
    num[f"Jogador {cont}"] = randint(1, 6)
    print(f'{f"Jogador {cont}"} tirou {num[f"Jogador {cont}"]}')
    cont += 1

print('-=-' * 10)
print('Ranking dos Jogadores:')
cont = 1
for c in sorted(num, key=num.get, reverse=True):
    print(f'{cont}° Lugar: {c} com {num[c]}')
    cont += 1
