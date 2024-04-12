contMaior = contHomem = contMulher = 0
esc = sexo = ''
while True:
    print('-=-' * 10)
    print('{:^30}'.format('CADASTRO DE PESSOAS'))
    print('-=-' * 10)

    idade = int(input(f'Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Sexo [M/F]: ')).upper()

    if idade > 18:
        contMaior += 1

    if sexo == 'M':
        contHomem += 1
    else:
        if idade < 20:
            contMulher += 1

    print('-=-' * 10)
    while esc != 'S' and esc != 'N':
        esc = str(input('Deseja continuar [S/N]? ')).upper()
    if esc == 'N':
        break
    esc = sexo = ''

print('-=-' * 10)
print(f'Pessoas Maiores de 18 anos: {contMaior}')
print(f'Homens cadastrados: {contHomem}')
print(f'Mulheres com menos de 20 anos: {contMulher}')
print('-=-' * 10)
