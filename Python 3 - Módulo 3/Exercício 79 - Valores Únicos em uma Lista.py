valores = []
esc = []
while True:
    a = int(input(f'Digite um número: '))
    if a in valores:
        print('Valor já foi adicionado na lista!')
    else:
        valores.append(a)
        print('Valor adicionado!')
    while esc != 'S' and esc != 'N':
        esc = str(input('Deseja continuar [S/N]? ')).upper()
    if esc == 'N':
        break
    esc = []

valores.sort()
print(f'\nLista: {valores}')
