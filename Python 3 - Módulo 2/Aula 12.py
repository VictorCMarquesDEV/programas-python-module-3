# elif -> else if
nome = str(input('Digite seu nome: '))
if nome == 'Victor':
    print('Que nome bonito.')
elif nome == 'Maria' or nome == 'João':
    print('Que nome comum.')
else:
    print('Que nome sem graça.')
print('Seja bem vindo, {}'.format(nome))
