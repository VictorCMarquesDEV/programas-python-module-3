import time
import random
print('-=-' * 10)
print('{:^30}'.format('Jokenpô'))
print('-=-' * 10)
time.sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = str(input('Escolha entre pedra, papel e tesoura: ')).upper()
pc = random.choice(lista)
print('\nJO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ\n')
time.sleep(1)

print('-=-' * 10)
print('Você escolheu {} e eu escolhi {}.'.format(jogador.upper(), pc))
if jogador == 'PEDRA' and pc == 'TESOURA':
    print('VOCÊ venceu! Parabéns!')
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('VOCÊ venceu! Parabéns!')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('VOCÊ venceu! Parabéns!')
elif jogador == pc:
    print('EMPATOU! Tente novamente!')
else:
    print('EU venci! Boa sorte na próxima!')
print('-=-' * 10)
