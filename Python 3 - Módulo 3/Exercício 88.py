from random import randint
from time import sleep

palpites = list()
numeros = list()
jogos = int(input('Quantos jogos serão gerados? '))

for c in range(0, jogos):
    for n in range(0, 6):
        a = randint(1, 60)
        while a in numeros:
            a = randint(1, 60)
        numeros.append(a)
    numeros.sort()
    palpites.append(numeros[:])
    numeros.clear()

print('-=-' * 15)
for c in range(0, jogos):
    sleep(1)
    print(f'Palpite {c + 1:2}: {palpites[c]}')
