from uteis import moedas

preco = float(input('Digite o preço: R$'))
print('=' * 50)
print(f'A metade de {moedas.fmt(preco)} é {moedas.metade(preco)}')
print(f'A dobro de {moedas.fmt(preco)} é {moedas.dobro(preco)}')
print(f'Aumentando 10% de {moedas.fmt(preco)} temos {moedas.aumentar(preco, 10)}')
print(f'Reduzindo 13% de {moedas.fmt(preco)} temos {moedas.diminuir(preco, 13)}')
