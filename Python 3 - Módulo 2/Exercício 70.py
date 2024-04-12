soma = menorP = cont = 0
esc = menorN = ''

print('-=-' * 10)
print('{:^30}'.format('FEIRA'))
print('-=-' * 10)

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if soma == 0:
        menorN = nome
        menorP = preco
    soma += preco

    if preco < menorP:
        menorP = preco
        menorN = nome
    if preco > 1000:
        cont += 1

    print('-=-' * 10)
    while esc != 'S' and esc != 'N':
        esc = str(input('Deseja continuar [S/N]? ')).upper()
    print('-=-' * 10)
    if esc == 'N':
        break
    esc = ''

print(f'Total gasto: R${soma:.2f}')
print(f'Produtos que custam mais de R$1.000: {cont}')
print(f'Produto mais barato: {menorN} -> R${menorP:.2f}')
print('-=-' * 10)
