from random import randint
contV = 0
s = ['PAR', 'IMPAR']

print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)

while True:
    jogador = str(input('Par ou Ímpar [P/I]? ')).upper()
    numJ = int(input('Digite um valor: '))
    numPC = randint(0, 10)
    print('-=-' * 10)
    print(f'\033[1;49;36mVocê escolheu {numJ} e o PC escolheu {numPC}\033[m.\nSoma = {numJ + numPC}', end=' ')
    if (numJ + numPC) % 2 == 0:
        vencedor = s[0]
        print(f'=> {vencedor}')
    else:
        vencedor = s[1]
        print(f'=> {vencedor}')
    if jogador in vencedor[0]:
        contV += 1
        print('\033[1;49;32mVocê VENCEU!\033[m\nVamos novamente...')
    else:
        print(f'\033[1;49;31mVocê PERDEU!\033[m\nObteve {contV} vitórias!')
        break
    print('-=-' * 10)
