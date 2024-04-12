# break -> sair do loop

cont = 1
while True:
    print(cont, ' ', end='')
    cont += 1
    if cont == 11:
        break

nome = 'José'
print(f'\n{nome} é o nome dele')
print('{} é o nome dele'.format(nome))
