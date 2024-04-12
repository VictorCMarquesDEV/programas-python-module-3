print('=' * 30)
print('{:^30}'.format('BANCO VCM'))
print('=' * 30)

valor = int(input('Qual valor a ser sacado? R$'))
c50 = valor / 50
c20 = (valor % 50) / 20
c10 = ((valor % 50) % 20) / 10
c1 = (((valor % 50) % 20) % 10) / 1

print('=' * 30)
print('Serão:')
if c50.__trunc__() != 0:
    print(f'{c50.__trunc__():2} cédula(s) de R$50')
if c20.__trunc__() != 0:
    print(f'{c20.__trunc__():2} cédula(s) de R$20')
if c10.__trunc__() != 0:
    print(f'{c10.__trunc__():2} cédula(s) de R$10')
if c1.__trunc__() != 0:
    print(f'{c1.__trunc__():2} cédula(s) de R$1')
print('=' * 30)
print('Volte sempre!')
