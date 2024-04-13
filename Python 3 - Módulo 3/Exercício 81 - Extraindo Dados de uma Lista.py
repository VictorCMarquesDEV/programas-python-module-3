valores = []
esc = []
while True:
    a = int(input(f'Digite um número: '))
    valores.append(a)
    while esc != 'S' and esc != 'N':
        esc = str(input('Deseja continuar [S/N]? ')).upper()
    if esc == 'N':
        break
    esc = []
a = valores[:]
valores.sort(reverse=True)
print(f'\nNúmeros Digitados: {len(valores)}')
print(f'Lista Decrescente: {valores}')
if 5 in a:
    print('5 está na lista nas posições ', end='')
else:
    print('5 NÃO está na lista!')
