pessoas = list()
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if cont == 0:
        maior = menor = dados[1]
    cont += 1
    if dados[1] > maior:
        maior = dados[1]
    if dados[1] < menor:
        menor = dados[1]
    dados.clear()
    esc = str(input('Você deseja continuar? '))
    if esc in 'Nn':
        break

print('-=-' * 50)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in range(0, len(pessoas)):
    if maior == pessoas[p][1]:
        print(f'[{pessoas[p][0]}]', end=' ')
print(f'\nO menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in range(0, len(pessoas)):
    if menor == pessoas[p][1]:
        print(f'[{pessoas[p][0]}]', end=' ')
