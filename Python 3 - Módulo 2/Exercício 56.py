soma = 0
qF = 0
maioridade = 0
maisvelho = 'Não existe homem neste grupo'
for c in range(1, 5):
    print('-' * 5 + ' {}º Pessoa '.format(c) + '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma += idade

    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            maisvelho = nome

    if sexo == 'F':
        if idade < 20:
            qF += 1

print('\nMédia da idade do grupo: {:.2f} anos'.format(soma / 4))
print('Homem mais velho: {}'.format(maisvelho), end='')
if maisvelho != 'Não existe homem neste grupo':
    print(' com {} anos'.format(maioridade), end='')
print('\nMulheres com menos de 20 anos: {}'.format(qF))
