sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('\nDigite novamente!')
    else:
        print('Seu sexo é [{}]'.format(sexo))
