import random
import time
num = random.randint(0, 10)
tent = 0
palpite = -1

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar... ')
print('-=-' * 20)

while palpite != num:
    palpite = int(input('Em que número eu pensei? '))
    print('-=-' * 20)
    time.sleep(1)
    tent += 1

    if palpite < 0 or palpite > 10:
        print('\nIntervalo inválido!')
    else:
        if palpite == num:
            print('\nPARABÉNS! Você me venceu!\nO número sorteado foi {}!'.format(palpite))
            print('Foi(ram) necessária(s) {} tentativa(s)!'.format(tent))
        else:
            print('TENTE NOVAMENTE! ', end='')
            if palpite > num:
                print('Dica: um pouco menos')
            else:
                print('Dica: um pouco mais')
